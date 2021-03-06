from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('upload', upload, name='upload'),
    path('<slug:audio_id>', audio, name='audio'),
]
