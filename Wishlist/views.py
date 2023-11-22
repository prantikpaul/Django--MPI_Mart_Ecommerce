from django.shortcuts import render,redirect
from Products.models import product
from . models import wishlist

# Create your views here.

def wishlistt(request):
    len_wlist=wishlist.objects.filter(user=request.user)
    if len_wlist:
        pass
        
    else:
        return redirect('wishlist_empty')
    

    return render (request,'Wishlist/wishlist.html',locals())

def wishlist_empty(request):
    

    return render (request,'Wishlist/wishlist_empty.html',locals())

def add_to_wishlist(request,id):
    prod=product.objects.get(id=id)

    if request.user.is_authenticated:

        if wishlist.objects.filter(product=prod).exists():
            pass
        else :
        
            Wlistt=wishlist.objects.create(
                user=request.user,
                product=prod
            )
            Wlistt.save()

    else:
        return redirect ('login')
    


    return redirect (request.META['HTTP_REFERER'])

def remove_wishlist_item(request,id):
    get_prod=wishlist.objects.filter(user=request.user, product=id)

    for i in get_prod :
        i.delete()
    

    return redirect (request.META['HTTP_REFERER'])