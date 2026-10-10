from django.contrib import admin
from .models import Product , ProductGaleryImage
# Register your models here.



class ProductAdmin(admin.ModelAdmin):

    list_display = ['__str__','id','title','slug', 'active','price']
    class Meta:
        model = Product
class ProductGaleryAdmin(admin.ModelAdmin):

    list_display = ['__str__','id','title', 'product','date_time_added','active']
    class Meta:
        model = ProductGaleryImage

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGaleryImage, ProductGaleryAdmin)






