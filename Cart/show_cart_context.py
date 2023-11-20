from Cart.models import cart




def show_cart(request):
    cartP=cart.objects.filter(user=request.user)
    total_prod=0
    for i in cartP:
        total_prod+=i.quantity
    data={
        'show_len_cart':total_prod,
    }

    return data
