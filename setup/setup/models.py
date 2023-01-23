from django.db import models
from django import view

class productMainModel(models.Model):
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=50)
    product_price = models.CharField(max_length=50)
    product_unique_code = models.BooleanField(null=True, blank=True)
    product_quality = models.CharField(max_length=200)
    CATEGORY_CHOICES = (
        ('H', 'High'),
        ('M', 'Mediume'),
        ('L', 'Low'),
    )

class productColourModel(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=50, null=True)

class productImageModel(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')