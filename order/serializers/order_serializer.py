from rest_framework import serializers

from order.models.order import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, required=True)
    products_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total
    
    class Meta:
        model = Product
        fields = ['product', 'total', 'user', 'products_id']
        extra_kwards = {'product': {'required': False}}

    def create(self, validated_data):
        products_data = validated_data.pop('product_id')
        user_data = validated_data.pop('user')

        order = Order.objects.create(user=user_data)
        for product in products_data:
            order.product.add(product)

        return order