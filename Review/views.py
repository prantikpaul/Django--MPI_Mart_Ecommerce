from django.shortcuts import render,redirect
from .models import prod_review
from Products.models import product
# Create your views here.

def get_review(request,id):
    
    if request.method=='POST':
        get_rating=request.POST['rating']
        get_comment=request.POST['comment']
        get_prod=product.objects.get(pk=id)
        
        if prod_review.objects.filter(prod=get_prod).exists():
            pass
        else :
            ppp=prod_review.objects.create(
                user=request.user,
                prod=get_prod,
                rating=get_rating,
                comment=get_comment,
            )
            ppp.save()
        


    
    return redirect (request.META['HTTP_REFERER'])