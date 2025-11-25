from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from accounts.models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "confirm_password"]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"password": "Password fields did not match"})
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        validated_data["password"] = make_password(validated_data["password"])
        return CustomUser.objects.create(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

class RefreshSerializer(serializers.Serializer):
    token = serializers.CharField(write_only=True)

class LogoutSerializer(serializers.Serializer):
    token = serializers.CharField(write_only=True)
