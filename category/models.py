from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    title=models.CharField(max_length=100 , verbose_name="عنوان دسته بندی")
    name=models.CharField(max_length=100,verbose_name="عنوان در یو از ال")

    def __str__(self):
        return self.title



    class Meta:
        verbose_name="دسته بندی"
        verbose_name_plural = "دسته بندی ها"