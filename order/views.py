from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from order.forms import UserNewOrderForm
from order.models import Order
from products.models import Product


@login_required(login_url='/login')
def add_new_order(request):
    # if not request.user.is_authenticated:
    #     return redirect('/login')
    new_order_form = UserNewOrderForm(request.POST or None)
    if new_order_form.is_valid():
        product_id = new_order_form.cleaned_data['product_id']
        product = Product.objects.get_product_by_id(product_id)
        if product is None:
            raise Http404("product not found")

        order = Order.objects.filter(user_id=request.user.id, paid=False).first()
        if order is None:
            order = Order.objects.create(user_id=request.user.id, paid=False)

        count = new_order_form.cleaned_data.get('count')
        if count < 1:
            count = 1
        order.orderdetail_set.create(order=order, product=product, count=count)
        return redirect(product.get_product_detail_url())

    return redirect('/')



@login_required(login_url='/login')
def card(request):
    context = {
        "order" : None ,
        "details" : None
    }

    open_order = order=Order.objects.filter(user_id=request.user.id).first()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()


    return render(request,"cart.html",context)