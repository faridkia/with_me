from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id']
    fieldsets = UserAdmin.fieldsets + (
        ('More info', {'fields': ['age'],}),
    )