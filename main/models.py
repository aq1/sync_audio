import random

from django.db import models
from django.utils.text import slugify


class Audio(models.Model):

    audio = models.FileField(upload_to='audio')
    slug = models.SlugField(
        db_index=True,
    )

    def save(self, **kwargs):
        self.slug = '{}-{}'.format(
            random.randint(9999, 999999),
            slugify(' '.join(self.audio.name.split('.')[:-1]), allow_unicode=True),
        )
        return super().save(**kwargs)
