from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Audio


def audio(request, audio_slug):
    _audio = Audio.objects.filter(slug=audio_slug).first()
    if not _audio:
        return redirect(reverse('index'))

    audios = Audio.objects.all()
    return render(request, 'main/audio.html', {'audio': _audio, 'audios': audios})


def index(request):
    audios = Audio.objects.all()
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
        return redirect(reverse('audio', kwargs={'audio_slug': _audio.slug}))

    return render(
        request,
        'main/index.html',
        {'errors': form.errors},
        status=400,
    )
