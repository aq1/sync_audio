from django.db import models

from ..models import Audio
from ..models import Directory


def get_sorted_audios(directory_id=None):
    directories = Directory.objects.all()
    if directory_id:
        directories = directories.filter(id=directory_id)

    audios = {
        directory: []
        for directory in directories
    }

    db_audios: models.QuerySet[Audio] = Audio.objects.select_related(
        'directory',
    ).filter(
        directory_id__in=directories.values_list('id', flat=True),
    ).order_by(
        'directory',
        'name',
    )

    for audio in db_audios:
        audios[audio.directory].append(audio)

    return list(audios.items())


def get_sorted_user_directories(user):
    return Directory.objects.filter(
        user=user,
    ).order_by(
        'name',
    )
