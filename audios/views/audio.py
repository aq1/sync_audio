from django.shortcuts import render, redirect
from django.urls import reverse

from ..models import Audio


def audio(request, audio_id, audio_slug):
    _audio = Audio.objects.filter(id=audio_id).first()
    if not _audio:
        return redirect(reverse('index'))

    audios = Audio.objects.exclude(
        id=_audio.id,
    ).order_by(
        '-pk',
    )
    return render(request, 'audios/audio.html', {'audio': _audio, 'audios': audios})
