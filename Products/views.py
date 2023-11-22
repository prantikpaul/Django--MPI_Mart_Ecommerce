from django.shortcuts import render
from .models import product
from Review.models import prod_review

# Create your views here.

def all_prod(request,id):
    show_prod=product.objects.filter(category=id).order_by('-created_at')
    FEATURED_1=product.objects.filter(featured_prod=True)[:3]
    FEATURED_2=product.objects.filter(featured_prod=True)[4:7]
    


    return render(request,'product/all_prod.html',locals())

def prod_view(request,id):
    show_signl_prod=product.objects.filter(id=id)

    show_review=prod_review.objects.filter(prod=id)
    
        


    return render(request,'product/single_prod_view.html',locals())

def empty_search(request):
    #for showing featured items -----------------------------------------
    FEATURED_1=product.objects.filter(featured_prod=True)[:3]
    FEATURED_2=product.objects.filter(featured_prod=True)[4:7]
    #for showing featured items -----------------------------------------

    return render(request,'product/empty_search.html',locals())