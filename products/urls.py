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
app_name = 'product'
from django.urls import path
from products.views import ProductsList,product_detail,SearchProducts,ProductsListByCategory


urlpatterns = [
    path('product_list', ProductsList.as_view(), name='produts_list'),
    path('product_detail/<product_id>/<title>',product_detail , name='product_detail'),
    path('product_search',SearchProducts.as_view() , name='search_product'),
    path('products_category/<category_name>',ProductsListByCategory.as_view() , name='category_product'),

]
