from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib import admin

from ..models import User


@admin.register(User)
class UserAdmin(UserAdminBase):
    pass
