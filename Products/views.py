from django.shortcuts import render
from .models import product

# Create your views here.

def all_prod(request,id):
    show_prod=product.objects.filter(category=id).order_by('-created_at')



    return render(request,'product/all_prod.html',locals())

def prod_view(request,id):
    show_signl_prod=product.objects.filter(id=id)
    

    return render(request,'product/single_prod_view.html',locals())