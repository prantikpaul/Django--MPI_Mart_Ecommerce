"""
URL configuration for MPI_Mart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('Cart/', include('Cart.urls')),
    path('Products/', include('Products.urls')),
    path('Accounts/', include('Accounts.urls')),
    path('Orders/', include('Orders.urls')),
    path('Payment/', include('Payment.urls')),
    path('Profile/', include('Profile.urls')),
    path('Review/', include('Review.urls')),
    path('Stuff_Panel/', include('Stuff_Panel.urls')),
    path('Wishlist/', include('Wishlist.urls')),
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
