from collections import defaultdict

from django.db import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..models import Audio
from ..models import Directory


def get_sorted_user_audios(user):
    directories = get_sorted_user_directories(user)
    audios = {
        directory.name: []
        for directory in directories
    }

    db_audios: models.QuerySet[Audio] = Audio.objects.select_related(
        'directory',
    ).filter(
        user=user,
    ).order_by(
        'directory',
        'name',
    )

    for audio in db_audios:
        audios[audio.directory.name].append(audio)

    return list(audios.items())


def get_sorted_user_directories(user):
    return Directory.objects.filter(
        user=user,
    ).order_by(
        'name',
    )
