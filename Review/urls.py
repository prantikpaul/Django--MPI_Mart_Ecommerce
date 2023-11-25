from django.urls import path
from . views import *


urlpatterns = [

    path('get_review/<int:id>/',get_review,name='get_review'),
    path('prod_avg_rater/<int:id>/',prod_avg_rater,name='prod_avg_rater'),

]
