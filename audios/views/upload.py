from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .utils import get_sorted_user_directories
from ..models import Audio
from ..models import Directory


class AudioForm(forms.ModelForm):
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
    files = request.FILES.getlist('audio')
    _forms = []
    _audio = None

    for _file in files:
        form = AudioForm(request.POST, {'audio': _file})
        form.fields['directory'].queryset = Directory.objects.filter(user=request.user)

        if not form.is_valid():
            return render(
                request,
                'audios/upload.html',
                context={
                    'directories': get_sorted_user_directories(request.user),
                    'errors': form.errors,
                },
                status=400,
            )
        else:
            _forms.append(form)

    if not _forms:
        return render(
            request,
            'audios/upload.html',
            context={
                'directories': get_sorted_user_directories(request.user),
                'errors': 'No files',
            },
            status=400,
        )

    for form in _forms:
        form.instance.user = request.user
        _audio = form.save()

    return redirect(reverse(
        'audios:audio',
        kwargs={
            'audio_slug': _audio.slug,
            'audio_id': _audio.id,
        },
    ))
