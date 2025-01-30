import json

from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from order.factories import UserFactory
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.token = Token.objects.create(user=self.user)
        self.category = CategoryFactory()
        self.product = ProductFactory.create(
            title="pro controller",
            price=200.00
        )
        self.product.category.add(self.category)

    def test_get_all_product(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response = self.client.get(
            reverse("product-list", kwargs={"version": "v1"})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(
            response_data['results'][0]["title"],
            self.product.title
        )

    def test_create_product(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        category = CategoryFactory()
        data = {
            "title": "notebook",
            "price": 800.00,
            "category": [category.id]
        }
        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)