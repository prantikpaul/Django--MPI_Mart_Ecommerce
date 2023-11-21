from .models import wishlist
from django.db.models import Count


def show_wishlist(request):
    try:
        wishP=wishlist.objects.filter(user=request.user)
        len_prod=len(wishP)
        
        data={
            'show_len_wishlist':len_prod,
        }

        return data
    except:
        len_prod=0
        data={
            'show_len_wishlist':len_prod,
        }

        return data