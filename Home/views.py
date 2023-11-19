from django.shortcuts import render
from Products.models import category,product

# Create your views here.
def home(request):
    
    

    return render(request,'home/index.html',locals())