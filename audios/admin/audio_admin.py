from django.contrib import admin
from django.urls import reverse, NoReverseMatch
from django.utils.safestring import mark_safe

from ..models import Audio


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'directory',
        'name',
        'url',
    ]

    list_filter = [
        'user',
        'directory',
    ]

    search_fields = [
        'user',
        'directory',
        'name',
    ]

    def url(self, obj: Audio):
        try:
            url = reverse('audios:audio', args=(obj.id, obj.slug))
        except NoReverseMatch:
            return 'Bad URL'
        return mark_safe(f'<a target="_blank" href="{url}">View on site</a>')


class AudioInline(admin.TabularInline):
    extra = 0
    fields = [
        'user',
        'audio',
        'name',
        'slug',
    ]
