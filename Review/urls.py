from django.urls import path
from . views import *


urlpatterns = [

    path('get_review/<int:id>/',get_review,name='get_review'),

]
