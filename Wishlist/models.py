from django.db import models
from Products.models import product
from django.contrib.auth.models import User
# Create your models here.

class wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name +'  '+ self.user.last_name 