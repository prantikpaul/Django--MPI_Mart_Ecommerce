from django.urls import path
from .views import *


urlpatterns = [
    path('checkout/',checkout,name='checkout'),
    path('place_order/<id>/',place_order,name='place_order'),
    path('order_success/',order_success,name='order_success'),
    path('order_save/',order_save,name='order_save'),
    path('order_details/<id>/',order_details,name='order_details'),

]
