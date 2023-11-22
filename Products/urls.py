from django.urls import path
from .views import *


urlpatterns = [
    path('all_products/<int:id>/',all_prod,name='all_prod'),
    path('prod_view/<int:id>/',prod_view,name='prod_view'),
    path('empty_search/',empty_search,name='empty_search'),

]
