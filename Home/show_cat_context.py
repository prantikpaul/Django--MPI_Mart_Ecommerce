from Products.models import category
from django.db.models import Count
def show_cat(request): #send category name with how many prod contain each category 
    categories_with_product_count = category.objects.annotate(num_products=Count('product'))
    data = {
        'show_cat': categories_with_product_count,
    }

    return data