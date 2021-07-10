from django.shortcuts import render, redirect
from django.urls import reverse

from .utils import get_sorted_user_audios
from ..models import Audio


def audio(request, audio_id, audio_slug):
    _audio = Audio.objects.filter(id=audio_id).first()
    if not _audio:
        return redirect(reverse('index'))

    audios = []
    if request.user.is_authenticated:
        audios = get_sorted_user_audios(request.user)

    return render(request, 'audios/audio.html', {'audio': _audio, 'audios': audios})
