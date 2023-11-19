from django.shortcuts import render
from .models import product

# Create your views here.

def all_prod(request,id):
    show_prod=product.objects.filter(category=id)
    


    return render(request,'product/all_prod.html',locals())