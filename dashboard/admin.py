from django.contrib import admin
from .models import VeterinaryOfficer

# Register your models here.


class VeterinaryOfficerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'county', 'idNo',
                    'mobile_number', 'is_active', 'date_joined')
    list_editable = ('email', 'county', 'idNo',
                     'mobile_number', 'is_active')


admin.site.register(VeterinaryOfficer, VeterinaryOfficerAdmin)
