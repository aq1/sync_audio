from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Audio


def audio(request, audio_id, audio_slug):
    _audio = Audio.objects.filter(id=audio_id).first()
    if not _audio:
        return redirect(reverse('index'))

    audios = Audio.objects.exclude(
        id=_audio.id,
    ).order_by(
        '-pk',
    )
    return render(request, 'main/audio.html', {'audio': _audio, 'audios': audios})


def index(request):
    audios = Audio.objects.all().order_by(
        '-pk',
    )
    return render(request, 'main/index.html', {'audios': audios})


class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = [
            'audio',
        ]


def upload(request):
    form = AudioForm(request.POST, request.FILES)
    if form.is_valid():
        _audio = form.save()
        return redirect(reverse(
            'audio',
            kwargs={
                'audio_slug': _audio.slug,
                'audio_id': _audio.id,
            },
        ))

    return render(
        request,
        'main/index.html',
        {'errors': form.errors},
        status=400,
    )
