from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from ..models import Audio


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ['slug', 'url']

    def url(self, obj: Audio):
        url = reverse('audios:audio', args=(obj.id, obj.slug))
        return mark_safe(f'<a target="_blank" href="{url}">{url}</a>')
