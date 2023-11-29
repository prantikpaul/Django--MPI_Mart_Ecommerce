from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
pp = (
    ('Pending','Pending'),
    ('Processing','Processing'),
    ('Completed','Completed'),
)


class Cart_order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_no=models.IntegerField()
    order_date=models.DateField(auto_now_add=True)
    order_status=models.CharField(choices=pp,default='Pending',max_length=20)
    total=models.IntegerField()
    total_item=models.IntegerField()

    def __str__(self):
        return self.user.first_name+' '+self.user.last_name
    

class Orders(models.Model):
    order_items=models.ForeignKey(Cart_order,on_delete=models.CASCADE)
    order_no=models.IntegerField()
    item=models.CharField(max_length=200)
    qyt=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()
    order_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_items.user.first_name+' '+self.order_items.user.last_name