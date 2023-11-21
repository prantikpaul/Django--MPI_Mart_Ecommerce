from django.shortcuts import render
from Products.models import category,product

# Create your views here.
def home(request):
    FEATURED_PRODUCTS=product.objects.filter(featured_prod=True)
    NEW_ARRIVALS=product.objects.filter(New_arrivals=True)
    BEST_SELLING_PRODUCTS=product.objects.filter(Best_selling_prod=True)
    
    

    return render(request,'home/index.html',locals())

