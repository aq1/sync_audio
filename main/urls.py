from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('upload', upload, name='upload'),
    path('<str:audio_slug>', audio, name='audio'),
]
