from product.models.category import Category
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    descvription = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveBigIntegerField(null=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category,blank=True)