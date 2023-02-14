from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ["username","email","is_active","age","is_staff","level"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age","level")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age","level")}),)