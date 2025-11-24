from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    confirm_password = serializers.CharField(write_only = True)

    
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "password", "confirm_password", "phone", "address", "birth_date")

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('Passwords do not match')
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('confrim_password')
        validated_data['password'] = make_password(validated_data['password'])
        user = CustomUser.objects.create(**validated_data)
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only = True)
    password = serializers.CharField(write_only = True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "phone", "address", "birth_date", "is_active")