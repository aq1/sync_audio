import os
import tempfile

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.core.files.uploadedfile import InMemoryUploadedFile


class Audio(models.Model):

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    directory = models.ForeignKey(
        'audios.Directory',
        on_delete=models.CASCADE,
    )

    audio = models.FileField(
        upload_to='audio',
    )

    slug = models.CharField(
        max_length=1000,
        db_index=True,
        blank=True,
    )

    name = models.CharField(
        max_length=255,
        default='',
        blank=True,
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True,
    )

    def save(self, **kwargs):
        self._convert_audio()
        self.name = ' '.join(self.audio.name.split('.')[:-1])
        self.slug = slugify(self.name, allow_unicode=True)
        return super().save(**kwargs)

    def __str__(self):
        return f'Audio {self.slug}'

    def _convert_audio(self):
        _audio = self.audio.file
        name = os.path.splitext(_audio.name)[0] + settings.DEFAULT_AUDIO_FORMAT
        with tempfile.TemporaryDirectory() as temp_dir:
            new_path = f'{temp_dir + "/" + name}'
            with tempfile.NamedTemporaryFile() as fp:
                fp.write(_audio.read())
                fp.seek(0)
                if os.system(f'ffmpeg -i "{fp.name}" "{new_path}"'):
                    return
                self.audio.name = name
                self.audio.file = InMemoryUploadedFile(
                    file=open(new_path, 'rb'),
                    field_name='audio',
                    name=name,
                    content_type='audio/mpeg',
                    size=_audio.size,
                    charset=_audio.charset,
                    content_type_extra=_audio.content_type_extra,
                )
