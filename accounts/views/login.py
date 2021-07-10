from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login

@require_http_methods(['GET'])
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('audios:index'))

    return render(request, 'accounts/login.html')


@require_http_methods(['POST'])
def login_submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        django_login(request, user)
        return redirect('audios:index')

    return render(request, 'accounts/login.html', {'error': 'Invalid password or username'})


@login_required
@require_http_methods(['POST'])
def logout(request):
    pass
