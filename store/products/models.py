from django.db import models

# Create your models here.
# модель = таблица


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)


class Product(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


