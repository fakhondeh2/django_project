from django.db import models

# Create your models here.

class ContactUs(models.Model):
     fullName = models.CharField(max_length=100 , null=False , verbose_name='نام کامل')
     email = models.EmailField( null=False, verbose_name='ایمیل')
     message = models.TextField(verbose_name="پیام")
     time = models.DateTimeField(auto_now_add=True)
     read = models.BooleanField(default=False, verbose_name="خوانده شده / خوانده نشده")


     class Meta:
         verbose_name="پیام"
         verbose_name_plural="پیام ها"


     def __str__(self):
         return self.fullName