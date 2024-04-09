from django.contrib import admin

from .models import CustomUser, CustomUserGroup

admin.site.register(CustomUser)
admin.site.register(CustomUserGroup)
