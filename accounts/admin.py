from django.contrib import admin

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_display_links = ('id', 'username')
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
