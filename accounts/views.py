from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status , permissions 
from rest_framework.response import Response
from django.contrib.auth import aauthenticate
from rest_framework_simplejwt.tokens import  RefreshToken
from .models import CustomUser
from .serializer import RegisterSerializer, LoginSerializer , UserSerializer


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self , request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully", "user": UserSerializer(user).data}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self , request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = aauthenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({'user': UserSerializer(user).data, 'access': str(refresh.access_tokan),'refresh': str(refresh)}, status=status.HTTP_200_OK)
            return Response({'detail': 'Invalid credentilas'}, status= status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self , request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"detail": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
