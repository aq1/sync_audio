from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse

from ..models import Audio


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
        'audios/index.html',
        {'errors': form.errors},
        status=400,
    )
