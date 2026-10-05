from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from category.models import ProductCategory
from .models import Product , ProductGaleryImage

# Create your views here.


class ProductsList(ListView):
    model = 'Product'
    template_name = 'products_list.html'
    paginate_by = 1

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductsListByCategory(ListView):
    template_name = 'products_list.html'
    paginate_by = 1

    def get_queryset(self):
        category_name= self.kwargs.get('category_name')
        categoryes = ProductCategory.objects.filter(name__iexact=category_name)
        if categoryes in None:
            raise Http404("محصولی با این دسته بندی یافت نشد")
        return Product.objects.get_product_by_category(category_name)


def products_category_partial(request):
    categoryes = ProductCategory.objects.all()

    context = {"categoryes":categoryes}
    return render(request,'categorys_view_partial.html',context)


def product_detail(request, product_id,title):
    product = Product.objects.get_product_by_id(product_id)
    galery = ProductGaleryImage.objects.get_galeryimage_product(product_id=product_id)
    context = {"product":product,
               "galery":galery}
    return render(request,'product_detail.html',context)


class SearchProducts(ListView):
    template_name = 'serch_page.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Product.objects.search_product(query)
        return Product.objects.get_active_products()
