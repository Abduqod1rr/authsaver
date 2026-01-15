from rest_framework import serializers
from .models import accdata

class AccDataSeriliazers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(sourse='owner.username')
    
    class Meta:
        model = accdata
        fields=['owner','title','acc_username','acc_password']
        read_only_fields=['owner']