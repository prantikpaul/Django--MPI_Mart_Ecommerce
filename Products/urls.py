from django.urls import path
from .views import *


urlpatterns = [
    path('products/<int:id>',all_prod,name='all_prod'),

]
