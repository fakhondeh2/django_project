from django.contrib.auth.models import User
from django.db import models

from products.models import Product


# Create your models here.

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="")
    paid = models.BooleanField(default=False,verbose_name="")
    pay_date = models.DateField(null=True , blank=True ,verbose_name="")


    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد های خرید"

    def __str__(self):
        return self.user.get_full_name()



class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="سبد خرید")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="محصول")
    count = models.IntegerField(default=0,verbose_name="تعداد")
    price = models.IntegerField(default=0,verbose_name="قیمت")

    class Meta:
        verbose_name = "محصول سبد خرید"
        verbose_name_plural="محصولات سبد خرید"

    def __str__(self):
        return self.product.title

    def product_sum_in_cart(self):
        return self.product.price * self.count