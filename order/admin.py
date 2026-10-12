from django.contrib import admin

from order.models import Order, OrderDetail


# Register your models here.



class OrderAdmin(admin.ModelAdmin):

    list_display = ['__str__','id','user','paid', 'pay_date']
    class Meta:
        model = Order
class OrderDetailAdmin(admin.ModelAdmin):

    list_display = ['__str__','id','order', 'product','count','price']
    class Meta:
        model = OrderDetail

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
