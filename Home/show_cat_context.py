from Products.models import category

def show_cat(request):
    show_cattP=category.objects.all()
    data={
        'show_cat': show_cattP,
    }

    return data