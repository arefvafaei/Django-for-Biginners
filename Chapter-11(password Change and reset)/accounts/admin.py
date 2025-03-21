from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeFrom, CustomUserCreateForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeFrom
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields" : ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields" : ("age",)}),)

admin.site.register(CustomUser, CustomUserAdmin)