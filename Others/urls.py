from django.urls import path
from .views import *


urlpatterns = [
    path('about_us/',about_us,name='about_us'),
    path('contact_us/',contact_us,name='contact_us'),
    path('blog/',blog,name='blog'),

]
