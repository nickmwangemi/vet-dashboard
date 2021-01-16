from django.contrib import admin
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile_number',
                    'is_active', 'date_joined')


admin.site.register(CustomUser, CustomUserAdmin)
