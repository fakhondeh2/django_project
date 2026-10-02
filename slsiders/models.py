import os
import random
from django.db import models

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


class Slsider(models.Model):
    title = models.CharField(max_length=200 , verbose_name="عنوان اسلایدر")
    link = models.URLField(max_length=200 , verbose_name="لینک اسلایدر")
    description = models.TextField(verbose_name="توضیحات اسلایدر")
    image = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name='آپلود عکس')
    active = models.BooleanField(default=True, verbose_name='فعال /غیر فعال')
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدر ها"

