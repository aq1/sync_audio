from django.contrib import admin

from ..models import Directory


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    search_fields = [
        'user',
        'name',
    ]

    list_display = [
        'user',
        'name',
    ]
