from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.login, name='login'),
    path('login/submit', views.login_submit, name='login_submit'),
    path('logout', views.logout, name='logout'),
]
