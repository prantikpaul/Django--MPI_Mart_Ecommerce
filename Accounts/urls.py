from django.urls import path
from .views import *


urlpatterns = [
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('verify_otp/',verify_otp,name='verify_otp'),
    path('logout/',logout,name='logout'),
    path('verify_token/<auth_token>/',verify,name='verify'),
    path('forget_pass/',forget_pass,name='forget_pass'),



]
