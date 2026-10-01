from django.contrib import admin

from category.models import ProductCategory


# Register your models here.


class ProductCategoryAdmin(admin.ModelAdmin):

    list_display = ['__str__','id','title', 'name']
    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)
