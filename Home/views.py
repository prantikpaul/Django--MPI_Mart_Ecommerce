from django.shortcuts import render,redirect
from Products.models import category,product

# Create your views here.
def home(request):
    FEATURED_PRODUCTS=product.objects.filter(featured_prod=True)
    NEW_ARRIVALS=product.objects.filter(New_arrivals=True)
    BEST_SELLING_PRODUCTS=product.objects.filter(Best_selling_prod=True)

    
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
                            

        
    
    

    return render(request,'home/index.html',locals())


def search(request,id,id2):
    #id = geting product name
    #id2 = geting category , if id2 is ==0 it's mean all category is selected , if 1 then phone cat ..... etc
    
    if int(id2)!=0 : # all category value is 0 , so if category is not 0 then search with category and name
        cat=product.objects.filter(category=id2 ,name__icontains=id) #filtering category first and then product
        if cat:
            pass
        else:
            return redirect('empty_search')  
                

    else: # if category is all category then search with name only 
        cat=product.objects.filter(name__icontains=id)
        if cat:
            pass
        else:
            return redirect('empty_search')       


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


    return render (request,'product/search.html',locals())