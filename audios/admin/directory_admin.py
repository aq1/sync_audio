from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from ..models import Directory


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']
