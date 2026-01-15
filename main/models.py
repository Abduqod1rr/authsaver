from django.db import models
from django.contrib.auth.models import User

class accdata(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=50, default="title 0")
    acc_username=models.CharField( max_length=5000,default='accname')
    acc_password=models.CharField( max_length=5000,default='accpassword')
    
    def __str__(self):
        return self.title
