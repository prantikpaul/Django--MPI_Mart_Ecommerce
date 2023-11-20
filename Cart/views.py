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