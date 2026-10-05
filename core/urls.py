"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import settings
from core.views import home,foter,heder,login,register,log_out
from products.views import products_category_partial
from contact_us.views import contact_us_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('products/', include('products.urls'),name='products'),
    path('products/', include('products.urls' , namespace='product')),
    path('', home, name='home'),
    path('heder', heder, name='heder'),
    path('foter', foter, name='foter'),
    path('contact_us', contact_us_view, name='contact_us'),
    path('login', login, name='login'),
    path('logout', log_out, name='logout'),
    path('register', register, name='register'),
    path('products_category_partial', products_category_partial, name='products_category_partial'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
