import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestOrderViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(
            title="mouse", price=100, category=[self.category]
        )
        self.order = OrderFactory(product=[self.product], user=self.user)

    def test_unauthorized_request(self):
        self.client.credentials()  # Remove credentials
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"})
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token invalid_token")
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"})
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_request(self):
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        order_data = json.loads(response.content)
        self.assertEqual(
            order_data["results"][0]["product"][0]["title"],
            self.product.title
        )

    def test_create_order_authenticated(self):
        data = {
            "product": [self.product.id],
            "user": self.user.id
        }
        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)