from django import forms
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

import magic

from .utils import get_sorted_user_directories
from ..models import Audio
from ..models import Directory


def audio_type_validator(obj):
    detected_type = magic.from_buffer(obj.read(5 * (1024 * 1024)), mime=True)
    obj.seek(0)

    if detected_type.split('/')[0] != 'audio':
        raise ValidationError(f'Bad mime type: {detected_type}')


class AudioForm(forms.ModelForm):
    audio = forms.FileField(
        validators=[
            audio_type_validator,
        ]
    )

    class Meta:
        model = Audio
        fields = [
            'directory',
            'audio',
        ]


@login_required
@require_http_methods(['GET'])
def upload(request):
    return render(
        request,
        'audios/upload.html',
        context={
            'directories': get_sorted_user_directories(request.user),
        }
    )


@login_required
@require_http_methods(['POST'])
def upload_submit(request):
    form = AudioForm(request.POST, request.FILES)
    form.fields['directory'].queryset = Directory.objects.filter(user=request.user)

    if form.is_valid():
        form.instance.user = request.user
        _audio = form.save()
        return redirect(reverse(
            'audios:audio',
            kwargs={
                'audio_slug': _audio.slug,
                'audio_id': _audio.id,
            },
        ))

    return render(
        request,
        'audios/upload.html',
        context={
            'directories': get_sorted_user_directories(request.user),
            'errors': form.errors,
        },
        status=400,
    )
