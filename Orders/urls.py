from django.urls import path
from .views import *


urlpatterns = [
    path('checkout/',checkout,name='checkout'),

]
