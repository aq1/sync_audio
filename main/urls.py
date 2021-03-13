from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('upload', upload, name='upload'),
    path('<int:audio_id>-<str:audio_slug>', audio, name='audio'),
]
