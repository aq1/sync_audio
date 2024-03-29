from django.shortcuts import render, redirect
from django.urls import reverse

from .utils import get_sorted_audios
from ..models import Audio


def audio(request, audio_id, audio_slug):
    _audio = Audio.objects.filter(id=audio_id).first()
    if not _audio:
        return redirect(reverse('index'))

    audios = get_sorted_audios(_audio.directory_id)

    previous, _next = None, None

    for audios_list in audios:
        for i, each in enumerate(audios_list[1]):
            if each.id != _audio.id:
                continue
            if i != 0:
                previous = audios_list[1][i - 1]
            try:
                _next = audios_list[1][i + 1]
            except IndexError:
                pass
            break

    return render(
        request,
        'audios/audio.html', {
            'audio': _audio,
            'audios': audios,
            'previous': previous,
            'next': _next,
        })
