from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User



class Userregister(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True)
    
    class Meta:
        model =User
        fields = ['username','password1','password2']
        extra_kwargs = {'password1': {'write_only': True}}
        
    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs 
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            
            password=validated_data['password1']
        )
        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token=super().get_token(user)
        token['username']= user.username
        return token

    
    