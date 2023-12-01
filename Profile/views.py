from django.shortcuts import render
from Accounts.models import Profile
from Orders.models import *

# Create your views here.
def user_profile(request):
    prof=Profile.objects.filter(user=request.user)


    # geting order history ------------------------
    get_cart_order=Cart_order.objects.filter(user=request.user)
    



    return render (request,'profile/profile.html',locals())