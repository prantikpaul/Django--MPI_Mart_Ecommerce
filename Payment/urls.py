from django.urls import path
from .views import *

urlpatterns = [
    path('payment/<id>/',payment,name='payment'),
    path('born_To_redirect/',born_To_redirect,name='born_To_redirect'),

]
