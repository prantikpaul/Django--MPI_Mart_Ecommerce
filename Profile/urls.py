from django.urls import path
from . views import *

urlpatterns = [
    path('user_profile/',user_profile,name='user_profile')

]
