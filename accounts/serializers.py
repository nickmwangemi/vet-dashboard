from rest_framework import serializers
from .models import CustomUser


class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('full_name',
                  'email',
                  'mobile_number',
                  'is_staff',
                  'is_active',
                  'date_joined',)
        model = CustomUser
