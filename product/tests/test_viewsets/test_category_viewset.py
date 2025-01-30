from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from product.factories import CategoryFactory

class TestCategoryViewSet(APITestCase):
    def setUp(self):
        self.category = CategoryFactory(title="technology")

    def test_get_all_category(self):
        response = self.client.get(
            reverse("category-list", kwargs={"version": "v1"})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(
            response_data['results'][0]["title"],
            self.category.title
        )