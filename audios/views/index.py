from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..models import Audio


@login_required
def index(request):
    audios = Audio.objects.all().order_by(
        '-pk',
    )
    return render(request, 'audios/index.html', {'audios': audios})
