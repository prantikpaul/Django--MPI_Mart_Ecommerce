from django.urls import path
from .views import*

urlpatterns = [
    path('wishlist/',wishlistt,name='wishlist'),
    path('wishlist_empty/',wishlist_empty,name='wishlist_empty'),
    path('add_to_wishlist/<int:id>/',add_to_wishlist,name='add_to_wishlist'),
    path('remove_wishlist_item/<int:id>/',remove_wishlist_item,name='remove_wishlist_item'),

]
