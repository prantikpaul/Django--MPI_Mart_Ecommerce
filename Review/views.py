from django.shortcuts import render,redirect
from .models import prod_review
from Products.models import product
# Create your views here.

def get_review(request,id):
    
    if request.method=='POST':
        get_rating=request.POST['rating']
        get_comment=request.POST['comment']
        get_prod=product.objects.get(pk=id)
        
        
        #convering ★★★★★ to int -----------------------
        int_rr=0
        if get_rating =='★★★★★':
            int_rr+=5
        elif get_rating =='★★★★':
            int_rr+=4
        elif get_rating =='★★★':
            int_rr+=3
        elif get_rating =='★★':
            int_rr+=2
        elif get_rating =='★':
            int_rr+=1
        # print(int_rr)

        ppp=prod_review.objects.create(
            user=request.user,
            prod=get_prod,
            rating=get_rating,
            comment=get_comment,
            int_rating=int_rr
        )
        ppp.save()

        return redirect ('prod_avg_rater',id)
        


    
    return redirect (request.META['HTTP_REFERER'])

def prod_avg_rater(request,id):
    get_prod=product.objects.get(pk=id)
        
    
            
    rrr=prod_review.objects.filter(prod=get_prod)
    if rrr :
        count=0
        for i in rrr:
            count+=1
        if count ==1  :
            rating=0
            for i in rrr:
                rating+=i.int_rating
            
            #for convert int to star :) 
            int_rr=''
            if rating ==5:
                int_rr+='★★★★★'
            elif rating ==4:
                int_rr+='★★★★'
            elif rating ==3:
                int_rr+='★★★'
            elif rating ==2:
                int_rr+='★★'
            elif rating ==1:
                int_rr+='★'
            # print(int_rr)
            rrr=product.objects.get(id=id) #geting product by id 
    
            if rrr: #upload product avg data to the product model
                rrr.avg_rating_star=int_rr
                rrr.avg_rating=rating
                rrr.save()
        
        elif count > 1 :
            rating=0
            # print(count)
            for i in rrr:
                rating+=i.int_rating
            avg_rating=rating/count
            rounded_number = round(avg_rating)
            # print(rounded_number)

            #for convert int to star :) 
            int_rr=''
            if rounded_number ==5:
                int_rr+='★★★★★'
            elif rounded_number ==4:
                int_rr+='★★★★'
            elif rounded_number ==3:
                int_rr+='★★★'
            elif rounded_number ==2:
                int_rr+='★★'
            elif rounded_number ==1:
                int_rr+='★'
            # print(int_rr)

            
            rrr=product.objects.get(id=id) #geting product by id 
    
            if rrr: #upload product avg data to the product model
                rrr.avg_rating_star=int_rr
                rrr.avg_rating=rounded_number
                rrr.save()
                        

            
    
    return redirect (request.META['HTTP_REFERER'])