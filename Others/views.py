from django.shortcuts import render

# Create your views here.

def blog(request):
    

    return render(request,'Others/blog.html',locals())

def about_us(request):
    

    return render(request,'Others/about_us.html',locals())

def contact_us(request):
    

    return render(request,'Others/contact_us.html',locals())