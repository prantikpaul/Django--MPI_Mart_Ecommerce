from django.urls import path
from .views import *


urlpatterns = [
    path('checkout/',checkout,name='checkout'),
    path('place_order/',place_order,name='place_order'),
    path('order_success/',order_success,name='order_success'),

]
