from rest_framework import serializers
from order.models import Order
from product.models import Product
from product.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        many=True
    )

    def get_total(self, instance):
        return sum([product.price for product in instance.product.all()])
    
    class Meta:
        model = Order
        fields = ['id', 'product', 'total', 'user', 'product_id']
        extra_kwargs = {'product': {'required': False}}

    def create(self, validated_data):
        product_data = validated_data.pop('product', [])
        user = validated_data.pop('user')
        
        order = Order.objects.create(user=user)
        
        if product_data:
            order.product.set(product_data)
        
        return order