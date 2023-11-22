from django.db import models
from Products.models import product
from django.contrib.auth.models import User


# Create your models here.

class prod_review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    prod=models.ForeignKey(product,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.CharField(max_length=400)
    date=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.prod.name+'---'+self.user.first_name+' '+self.user.last_name