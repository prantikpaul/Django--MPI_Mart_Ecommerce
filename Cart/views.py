from django.shortcuts import render,redirect
from .models import cart
from Products.models import product
from django.contrib import messages



# Create your views here.

def add_to_cart(request,id):
    prod=product.objects.get(pk=id)

    try:  
        ppp= cart.objects.filter(user=request.user, product=prod).first()
        if ppp:
            try:
                if request.method=='POST': #jodi single page view theke quantity ashe tahole :
                    get_quty=request.POST['quantity']
                    ppp.quantity+=int(get_quty)
                    ppp.save()
            except:
                ppp.quantity+=1
                ppp.save()

        else: 
            add_cart=cart.objects.create(user=request.user , product=prod)
            add_cart.save()
                
    except:
        messages.warning(request, "To Add Items To Your Cart ,Please Log in")
        return redirect ('login')
    
    return redirect (request.META['HTTP_REFERER'])


def view_cart(request):
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


    

    return render (request,'cart/view_cart.html',locals())

def empty_cart(request):
    
    return render(request,'cart/empty_cart.html')