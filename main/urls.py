from django.contrib import admin
from django.http import FileResponse
from django.shortcuts import render
from django.urls import path, include
from django.conf import settings


def a(request):
    return FileResponse(open(settings.BASE_DIR / 'Draft Impala.mp3', 'rb'))


def index(request):
    return render(request, 'main/index.html')


urlpatterns = [
    path('', index),
    path('a', a),
]
