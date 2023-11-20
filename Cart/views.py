from django.shortcuts import render,redirect
from .models import cart
from Products.models import product
from django.contrib import messages



# Create your views here.

def add_to_cart(request,id):
    prod=product.objects.get(pk=id)
    try:  
        ppp= cart.objects.filter(user=request.user, product=prod).first()
        if ppp:
            try:
                if request.method=='POST': #jodi single page view theke quantity ashe tahole :
                    get_quty=request.POST['quantity']
                    ppp.quantity+=int(get_quty)
                    ppp.save()
                else:
                    ppp.quantity+=1
                    ppp.save()
            except:
                pass

        else: 
            add_cart=cart.objects.create(user=request.user , product=prod)
            add_cart.save()
                
    except:
        messages.warning(request, "To Add Items To Your Cart ,Please Log in")
        return redirect ('login')
    
    return redirect (request.META['HTTP_REFERER'])


def view_cart(request):
    if request.user.is_authenticated:
        
        cart_len=cart.objects.filter(user=request.user)
        prod_len_conunt=0 # collecting prod id if avaiable
        for i in cart_len :
            prod_len_conunt+=i.id # add prod id if avaiaable
            
        if prod_len_conunt>0: #if prod exisit in cart then show view cart page 
         
            all_prod=cart.objects.filter(user=request.user)
            total_amnt=0
            for i in all_prod :
                total_amnt+=i.product.price*i.quantity
            try:
                if request.method=='POST':
                    ppp=request.POST['coupon_code']
                    print(ppp)
            except:
                pass
            
            total_with_shipping=total_amnt+100

        else: #if prod don't exisit in cart then show empty cart page 
            return redirect('empty_cart')

    else:
        return redirect ('index')


    

    return render (request,'cart/view_cart.html',locals())

def empty_cart(request):
    
    return render(request,'cart/empty_cart.html')

def cart_clear(request,id):
  #cart er X button click korle product remove kore dibe ... 
    ppq=cart.objects.filter(user=request.user , product=id)
    for i in ppq:
        i.delete()
        

    
    return redirect (request.META['HTTP_REFERER'])

def update_cart_qnty(request,id,action):
    
    prod = cart.objects.get(product=id, user=request.user) #cart er kon user kon prod er qun up korte chay ta get korbe
    if action == 'plus': # jodi - button a chap dey
        prod.quantity += 1

    elif action == 'minus': # jodi + button a chap dey
        if prod.quantity > 1:
            prod.quantity -= 1

        else:
            prod.delete()
            return redirect (request.META['HTTP_REFERER'])
    prod.save()
     
    
    return redirect (request.META['HTTP_REFERER'])