from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UsersAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_admin', 'is_doctor', 'is_client', 'is_staff', 'last_login')
    search_fields = ('username', 'first_name')
    readonly_fields = ('is_staff', 'last_login', 'date_joined')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()

    ordering = ('username',)


admin.site.register(User, UsersAdmin)