from django.test import TestCase
from product.serializers import ProductSerializer
from product.models import Product
from product.factories import ProductFactory, CategoryFactory

class TestProductSerializer(TestCase):
    def setUp(self):
        self.category = CategoryFactory(title="technology")
        self.product_1 = ProductFactory(title="mouse", price=100)
        self.product_1.category.add(self.category)
        self.product_serializer = ProductSerializer(instance=self.product_1)

    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data["title"], "mouse")
        self.assertEqual(serializer_data["price"], 100)
        self.assertEqual(serializer_data["category"][0]["title"], "technology")