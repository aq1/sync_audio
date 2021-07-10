from django.db import models


class Directory(models.Model):

    name = models.CharField(
        max_length=200,
        unique=True,
    )

    def __str__(self):
        return f'Directory {self.name}'
