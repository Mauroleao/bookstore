from rest_framework import serializers
from order.models import Order
from product.models import Product
from product.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'product', 'user', 'created_at', 'updated_at']