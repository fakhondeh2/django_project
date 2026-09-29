from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Product

# Create your views here.


class ProductsList(ListView):
    model = 'ModelName'
    template_name = 'products_list.html'
    paginate_by = 1

    def get_queryset(self):
        return Product.objects.get_active_products()



def product_detail(request, product_id,title):
    print(product_id)
    print(title)
    product = Product.objects.get_product_by_id(product_id)
    print(product)
    context = {"product":product}
    return render(request,'product_detail.html',context)


class SearchProducts(ListView):
    template_name = 'products_list.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Product.objects. filter(title__icontains=query)
        return Product.objects.get_active_products()
