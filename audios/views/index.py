from django.shortcuts import render

from .utils import get_sorted_audios


def index(request):
    audios = get_sorted_audios()
    return render(request, 'audios/index.html', {'audios': audios})
