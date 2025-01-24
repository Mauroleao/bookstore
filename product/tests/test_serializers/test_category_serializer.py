from django.test import TestCase
from product.serializers import CategorySerializer
from product.models import Category
from product.factories import CategoryFactory

class TestCategorySerializer(TestCase):
    def setUp(self):
        self.category = CategoryFactory(title="food")
        self.category_serializer = CategorySerializer(instance=self.category)

    def test_order_serializer(self):
        serializer_data = self.category_serializer.data
        self.assertEqual(serializer_data["title"], "food")