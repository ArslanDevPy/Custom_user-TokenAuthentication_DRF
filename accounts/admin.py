from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as User_Admin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class UserAdmin(User_Admin):
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
