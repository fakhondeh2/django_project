from django.db import models
from django.db.models.signals import pre_save

from products.models import Product
from .utils import unique_slug_generator


# Create your models here.
class Tag(models.Model):
    title=models.CharField(max_length=100,verbose_name="عنوان")
    slug=models.SlugField(unique=True,blank=True,allow_unicode=True,verbose_name="عنوان در آدرس url")
    active=models.BooleanField(default=True, verbose_name="فعال/غیر فعال")
    time=models.DateTimeField(auto_now_add=True)
    products=models.ManyToManyField(Product,blank=True,verbose_name="اتصال به محصولات")




    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تگ/برچسب"
        verbose_name_plural = "تگ ها / برچسب ها"



def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    current_slug = instance.slug or None
    instance.slug = unique_slug_generator(instance, new_slug=current_slug)


pre_save.connect(tag_pre_save_receiver,sender=Tag)