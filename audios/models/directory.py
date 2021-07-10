from django.contrib.auth import get_user_model
from django.db import models


class Directory(models.Model):

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=200,
        unique=True,
    )

    class Meta:
        verbose_name_plural = 'Directories'
        unique_together = (
            ('user', 'name'),
        )

    def __str__(self):
        return f'Directory {self.name}'
