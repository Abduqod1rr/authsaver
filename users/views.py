from django.shortcuts import render
from rest_framework import generics , permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import Userregister , TokenObtainPairSerializer ,CustomTokenObtainPairSerializer
from django.contrib.auth.models import User

class Register(generics.CreateAPIView):
    queryset = User.objects.all
    serializer_class = Userregister
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class  = CustomTokenObtainPairSerializer