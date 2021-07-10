from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .utils import get_sorted_user_audios


@login_required
def index(request):
    audios = get_sorted_user_audios(request.user)
    return render(request, 'audios/index.html', {'audios': audios})
