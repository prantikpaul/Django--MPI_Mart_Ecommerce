from django.shortcuts import render,redirect
from .models import prod_review
from Products.models import product
# Create your views here.

def get_review(request,id):
    
    if request.method=='POST':
        get_rating=request.POST['rating']
        get_comment=request.POST['comment']
        get_prod=product.objects.get(pk=id)
        
        # if prod_review.objects.filter(user=request.user).exists():
        #     pass
        # # else:
            
        #     # rrr=prod_review.objects.filter(prod=get_prod)
        #     # if rrr :
        #     #     count=0
        #     #     for i in rrr:
        #     #         count+=1
        #     #     # print(count)
        #     #     if count ==1  :
        #     #         rating=0
        #     #         for i in rrr:
        #     #             rating+=i.rating
                
        #     #     elif count > 1 :
        #     #         rating=0
        #     #         print(count)
        #     #         for i in rrr:
        #     #             rating+=i.rating
        #     #         avg_rating=rating/count
        #     #     print(type(rating))
        #     #     print(avg_rating)
                        
        # else :
        # rrr=prod_review.objects.filter(prod=get_prod)
        # if rrr :
        #     count=0
        #     for i in rrr:
        #         count+=1
        #     # print(count)
        #     if count ==1  :
        #         rating=0
        #         for i in rrr:
        #             rating+=i.rating
        #         ppp=prod_review.objects.create(
        #             user=request.user,
        #             prod=get_prod,
        #             rating=get_rating,
        #             comment=get_comment,
        #             avg_rating=rating,
        #         )
        #         ppp.save()
            
        #     elif count > 1 :
        #         rating=0
        #         print(count)
        #         for i in rrr:
        #             rating+=i.rating
        #         avg_rating=rating/count
        #         rounded_number = round(avg_rating)
        #         ppp=prod_review.objects.create(
        #             user=request.user,
        #             prod=get_prod,
        #             rating=get_rating,
        #             comment=get_comment,
        #             avg_rating=rounded_number
        #         )
        #         ppp.save()
        #     print(type(rating))
        #     print(avg_rating)


        ppp=prod_review.objects.create(
            user=request.user,
            prod=get_prod,
            rating=get_rating,
            comment=get_comment,
        )
        ppp.save()
        


    
    return redirect (request.META['HTTP_REFERER'])