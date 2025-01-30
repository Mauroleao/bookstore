from django.db import models

class Order(models.Model):
    product = models.ManyToManyField("product.Product", related_name="orders")
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="orders"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
