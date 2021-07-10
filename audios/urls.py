from django.urls import path

from . import views

app_name = 'audios'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('upload_submit', views.upload_submit, name='upload_submit'),
    path('directory', views.directory, name='directory'),
    path('directory_submit', views.directory_submit, name='directory_submit'),
    path('audios/<int:audio_id>-<str:audio_slug>', views.audio, name='audio'),
]
