from rest_framework import serializers
from .models import CustomUser
from .account_utils import AccountUtils

class CustomUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length = 8, write_only = True)
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'password',
            'is_admin',
            'profile_image',
        ]
    
    def validate_password(self, value):
       return AccountUtils.validate_password(value)
    
