from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout


def _get_redirect_location(request):
    return request.GET.get(
        'next',
        reverse('audios:index'),
    )


@require_http_methods(['GET'])
def login(request):
    if request.user.is_authenticated:
        return redirect(_get_redirect_location(request))

    return render(request, 'accounts/login.html')


@require_http_methods(['POST'])
def login_submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        django_login(request, user)
        return redirect(_get_redirect_location(request))

    return render(request, 'accounts/login.html', {'error': 'Invalid password or username'})


@login_required
@require_http_methods(['GET'])
def logout(request):
    django_logout(request)
    return redirect(_get_redirect_location(request))
