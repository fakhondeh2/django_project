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
    final_name = f"{instance.id}-{rand_name}{ext}"
    return f"setting/{final_name}"




class Settings(models.Model):
    email = models.EmailField(verbose_name="ایمیل مجموعه")
    phone = models.CharField(max_length=200,verbose_name="شماره مجموعه")
    mobile = models.CharField(max_length=200,verbose_name="شماره همراه مجموعه")
    fax = models.CharField(max_length=150,verbose_name="شماره فکس مجوعه")
    address = models.CharField(max_length=200,verbose_name="آدرس مجموعه")
    copy_right = models.CharField(max_length=200,verbose_name="متن کپی رایت")
    about = models.TextField(verbose_name="متن درباره ما")
    instagram = models.CharField(max_length=200,verbose_name="آدرس اینستا گرام")
    logo = models.ImageField(upload_to=upload_image, null=True, blank=True , verbose_name='لوگو مجموعه')



    class Meta:
        verbose_name = "تنظیمات"
        verbose_name_plural = "تنظیمات"

    def __str__(self):
        return str(self.id)
