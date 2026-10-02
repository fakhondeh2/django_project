import os
import random
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save

from category.models import ProductCategory
from .utils import unique_slug_generator
from django.urls import reverse


# Create your models here.


def get_file_extension(filename):
    Base_name = os.path.basename(filename)
    name, ext = os.path.splitext(Base_name)
    return name, ext


def upload_image(instance, filename):
    rand_name = random.randint(1, 9999999999999999999999)
    name, ext = get_file_extension(filename)
    final_name = f"{instance.id}-{instance.title}-{rand_name}{ext}"
    return f"products/{final_name}"




class Productmanager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)


    def get_product_by_id(self,product_id):
        qr = self.get_queryset().filter(id=product_id,active=True)
        if qr.count()==1:
            return qr.first()
        else:
            return None


    def search_product(self,query):
        lookup = Q(title__icontains=query) | Q(description__icontains=query) | Q(tag__title__icontains=query)
        return self.get_queryset().filter(lookup,active=True).distinct()



    def get_product_by_category(self,category_name):
        return self.get_queryset().filter(category__name__iexact=category_name)




class Product(models.Model):
    title = models.CharField(verbose_name='عنوان')
    slug = models.SlugField(unique=True, blank=True ,allow_unicode=True, verbose_name='اسلاگ')
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=50, decimal_places=2 , verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image, null=True, blank=True , verbose_name='آپلود عکس')
    active = models.BooleanField(default=True , verbose_name='فعال /غیر فعال')
    date_time_added = models.DateTimeField(auto_now_add=True )
    category=models.ManyToManyField(ProductCategory , blank=True,verbose_name="اضافه کردن دسته بندی"
                                                                              "")


    objects = Productmanager()



    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title

    def get_product_detail_url(self):
        return reverse('product:product_detail', kwargs={
            'product_id': self.id,
            'title': self.slug  # یا self.title، بسته به چی می‌خوای توی URL بیاد
        })


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    current_slug = instance.slug or None
    instance.slug = unique_slug_generator(instance, new_slug=current_slug)


pre_save.connect(product_pre_save_receiver, sender=Product)
