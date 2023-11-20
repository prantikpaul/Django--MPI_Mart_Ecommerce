from django.urls import path
from .views import *


urlpatterns = [
    path('add_to_cart/<int:id>/',add_to_cart,name='add_to_cart'),
    path('view_cart/',view_cart,name='view_cart'),
    path('empty_cart/',empty_cart,name='empty_cart'),
    path('cart_clear/<id>/',cart_clear,name='cart_clear'),
    path('update_cart_qnty/<int:id>/<str:action>/',update_cart_qnty,name='update_cart_qnty'),

]
