from django.db import models
from django.contrib.auth.models import User
from Products.models import product

# Create your models here.

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    def __str__(self):
      return self.user.first_name+''+self.user.last_name
    
    def total_price(self) :
       return self.product.price*self.quantity