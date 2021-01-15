from rest_framework import serializers
from dashboard.models import VeterinaryOfficer


class VeterinaryOfficerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'email', 'county', 'idNo',
                  'mobile_number', 'is_active', 'date_joined')
        model = VeterinaryOfficer
