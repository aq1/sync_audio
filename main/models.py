import os
import tempfile

from django.db import models
from django.utils.text import slugify
from django.core.files.uploadedfile import InMemoryUploadedFile


class Audio(models.Model):

    audio = models.FileField(
        upload_to='audio',
    )
    slug = models.SlugField(
        db_index=True,
    )

    def save(self, **kwargs):
        self._convert_audio()
        self.slug = slugify(' '.join(self.audio.name.split('.')[:-1]), allow_unicode=True)
        return super().save(**kwargs)

    def __str__(self):
        return self.slug

    def _convert_audio(self):
        _audio = self.audio.file
        name = os.path.splitext(_audio.name)[0] + '.mp3'
        with tempfile.TemporaryDirectory() as temp_dir:
            new_path = f'{temp_dir + "/" + name}'
            with tempfile.NamedTemporaryFile() as fp:
                fp.write(_audio.read())
                fp.seek(0)
                os.system(f'ffmpeg -i "{fp.name}" "{new_path}"')
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
                print()
