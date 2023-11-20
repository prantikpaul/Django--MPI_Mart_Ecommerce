from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(category)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','price','category','quantity','featured_prod','New_arrivals','Best_selling_prod','created_at') 
    list_editable=('price','quantity','featured_prod','New_arrivals','Best_selling_prod')
admin.site.register(product,ProductAdmin)

# Register your models here.
