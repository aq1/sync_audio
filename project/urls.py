from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


def webhook(request):
    with open('log.txt', 'a') as f:
        f.write(f'{request.POST}\n\n{request.body}\n\n')

    return HttpResponse('')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('webhook', webhook),
    path('', include('audios.urls', namespace='audios')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
