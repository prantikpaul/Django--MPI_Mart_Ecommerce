from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from Accounts.models import Profile
from Cart.models import cart
from .models import *
import random

# Create your views here.

def checkout(request):
    #to show User data in Billing details
    get_user=User.objects.get(id=request.user.id)
    
    #to show User Profile data in Billing details
    get_prof=Profile.objects.get(user=request.user.id)

    if request.user.is_authenticated:
        
        cart_len=cart.objects.filter(user=request.user)
            
        if cart_len: #if prod exisit in cart then show view cart page 
         
            all_prod=cart.objects.filter(user=request.user)
            total_amnt=0
            for i in all_prod :
                total_amnt+=i.product.price*i.quantity
            try:
                if request.method=='POST':
                    ppp=request.POST['coupon_code']
                    print(ppp)
            except:
                pass
            
            total_with_shipping=total_amnt+100

        else: #if prod don't exisit in cart then show empty cart page 
            return redirect('empty_cart')

    else:
        return redirect ('index')
    
    
    

    return render (request,'order/checkout.html',locals())

def place_order(request,id):
    if request.method=='POST':
        pp=request.POST['shipping_method[0]']
        print(pp)
        if pp =='payment_online':
            return redirect ('payment',id)
        else:
            return redirect ('order_save')
    

    return redirect (request.META['HTTP_REFERER'])

def order_success(request):
    

    return render(request,'order/order_success.html',locals())


def order_save(request):
    get_cart=cart.objects.filter(user=request.user)
    
    total_imt=0
    total=0
    for i in get_cart:
        total+=i.product.price*i.quantity
        total_imt+=i.quantity
    print(total)
    print(total_imt)

    ord_no=random.randint(1111,9999)
    print(ord_no)
    ppp=Cart_order.objects.create(
        user=request.user,
        order_no=ord_no,
        total=total,
        total_item=total_imt,
    )
    ppp.save()

    for i in get_cart:
        oders=Orders.objects.create(
            order_by_user=ppp,
            order_no=ord_no,
            item=i.product.name,
            qyt=i.quantity,
            price=i.product.price,
            total=total,
        )
        oders.save()

    get_cart.delete()

    return redirect('order_success')

def order_details(request):
    

    return render(request,'order/order_details.html')