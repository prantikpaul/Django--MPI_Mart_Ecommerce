from django.urls import path

from . views import home,search

urlpatterns = [
    
    path('',home,name='index'),
    path('search/<id>/<id2>/',search,name='search'),
]
