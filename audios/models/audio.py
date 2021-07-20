import io

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.core.files.uploadedfile import InMemoryUploadedFile

from ..utils import convert_audio


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
        name, audio_bytes = convert_audio(self.audio.file)
        self.audio.name = name
        self.audio.file = InMemoryUploadedFile(
            file=io.BytesIO(audio_bytes),
            field_name='audio',
            name=name,
            content_type=None,
            size=len(audio_bytes),
            charset=None,
            content_type_extra=None,
        )
