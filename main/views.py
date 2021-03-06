from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Audio


def audio(request, audio_id):
    _audio = get_object_or_404(Audio, slug=audio_id)
    return render(request, 'main/audio.html', {'audio': _audio})


def index(request):
    return render(request, 'main/index.html')


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
        return redirect(reverse('audio', kwargs={'audio_id': _audio.slug}))

    return render(
        request,
        'main/index.html',
        {'errors': form.errors},
        status=400,
    )
