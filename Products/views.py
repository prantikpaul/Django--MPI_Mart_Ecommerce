from django.shortcuts import render,redirect
from .models import product,category
from Review.models import prod_review

# Create your views here.

def all_prod(request,id):
    show_prod=product.objects.filter(category=id).order_by('-created_at')
    FEATURED_1=product.objects.filter(featured_prod=True)[:3]
    FEATURED_2=product.objects.filter(Best_selling_prod=True)[4:7]

    show_cat_nm=category.objects.filter(id=id) #to show category name in title 
    rrr=''
    for i in show_cat_nm: 
        rrr=i.name


        #for search bar --------------------------------------------------------
    try:
        if request.method=='GET':
            pp=request.GET['search'] #geting prod name
            rr=int(request.GET['product_cat']) # get category name
            
            if pp :
                print('okkk')
                return redirect('search',pp,rr)
    except:
        pass
    
    #for search bar --------------------------------------------------------
    


    return render(request,'product/all_prod.html',locals())

def prod_view(request,id):
    show_signl_prod=product.objects.filter(id=id)

    ppp = ''

    for i in show_signl_prod : #to show title name of that product 
        ppp=i.name

    show_rating=prod_review.objects.filter(prod=id)
    count_review = 0  # count how many reviews this prod has
    for i in show_rating:
        count_review+=1
        
        #for search bar --------------------------------------------------------
    try:
        if request.method=='GET':
            pp=request.GET['search'] #geting prod name
            rr=int(request.GET['product_cat']) # get category name
            
            if pp :
                print('okkk')
                return redirect('search',pp,rr)
    except:
        pass
    
    #for search bar --------------------------------------------------------
    
   
    
        


    return render(request,'product/single_prod_view.html',locals())

def empty_search(request):
    #for showing featured items -----------------------------------------
    FEATURED_1=product.objects.filter(featured_prod=True)[:3]
    FEATURED_2=product.objects.filter(featured_prod=True)[4:7]
    #for showing featured items -----------------------------------------

        #for search bar --------------------------------------------------------
    try:
        if request.method=='GET':
            pp=request.GET['search'] #geting prod name
            rr=int(request.GET['product_cat']) # get category name
            
            if pp :
                print('okkk')
                return redirect('search',pp,rr)
    except:
        pass
    
    #for search bar --------------------------------------------------------
    
    return render(request,'product/empty_search.html',locals())