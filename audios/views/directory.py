from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from ..models import Directory
from .utils import get_sorted_audios


class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = [
            'name',
        ]


@login_required
@require_http_methods(['GET'])
def directory(request):
    return render(
        request,
        'audios/directory.html',
        context={
            'audios': get_sorted_audios(),
        },
    )


@login_required
@require_http_methods(['POST'])
def directory_submit(request):
    form = DirectoryForm(request.POST)
    if form.is_valid():
        form.instance.user = request.user
        _directory = form.save()
        return redirect(reverse(
            'audios:directory',
        ))

    return render(
        request,
        'audios/directory.html',
        context={
            'audios': get_sorted_audios(),
        },
        status=400,
    )
