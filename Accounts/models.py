from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    auth_token = models.CharField(max_length=100)
    is_token_verified = models.BooleanField(default=False)
    otp=models.CharField(max_length=6)
    sign_in_otp_verify= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    Address1=models.CharField(max_length=200)
    Address2=models.CharField(max_length=200,blank=True,null=True)
    phone=models.CharField(max_length=20)

    def __str__(self):
        return self.user.first_name +'  '+ self.user.last_name 


