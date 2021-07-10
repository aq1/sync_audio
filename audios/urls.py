from django.urls import path

from .views import *

app_name = 'audios'

urlpatterns = [
    path('', index, name='index'),
    path('upload', upload, name='upload'),
    path('audios/<int:audio_id>-<str:audio_slug>', audio, name='audio'),
]
