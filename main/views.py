from django.shortcuts import render
from .models import accdata 
from .serializer import AccDataSeriliazers
from rest_framework.generics import CreateAPIView ,DestroyAPIView
from .permissions import IsOwner


class createData(CreateAPIView):
    queryset = accdata.objects.all()
    serializer_class = AccDataSeriliazers
    permission_classes = [IsOwner]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)