from django.shortcuts import render, redirect

from order.forms import UserNewOrderForm
from order.models import Order
from products.models import Product


# Create your views here.

def add_new_order(request):
    new_order_form=UserNewOrderForm(request.POST or None)
    if new_order_form.is_valid():
        order=Order.objects.filter(user_id=request.user.id , paid=False).first()
        if order is None:
            order = Order.objects.create(user_id=request.user.id , paid=False)
            order.save()
            product_id = new_order_form.cleaned_data['product_id']
            product = Product.objects.get_product_by_id(product_id)
            count = new_order_form.cleaned_data.get('count')
            if count < 0:
                count = 1
            order.orderdetail_set.create(order=order, product=product, count=count)

        product_id=new_order_form.cleaned_data['product_id']
        product = Product.objects.get_product_by_id(product_id)
        count = new_order_form.cleaned_data.get('count')
        if count < 0:
            count = 1
        order.orderdetail_set.create(order=order,product=product,count=count)

    return redirect(f"products/product_detail/{product_id}/{product.title.replace(" ","-")}")