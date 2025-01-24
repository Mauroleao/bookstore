import json

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from product.factories import CategoryFactory
from product.models import Category


class CategoryViewSet(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = CategoryFactory(title="technology")

    def test_get_all_category(self):
        response = self.client.get(reverse("category-list", kwargs={"version": "v1"}))
        self.assertEqual(response.status_code, 200)

    def test_create_category(self):
        data = {"title": "technology"}
        response = self.client.post(reverse("category-list", kwargs={"version": "v1"}), data, format='json')
        self.assertEqual(response.status_code, 201)