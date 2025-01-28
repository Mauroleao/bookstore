from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from product.factories import CategoryFactory
from product.models import Category

class TestCategoryViewSet(APITestCase):
    def setUp(self):
        self.category = CategoryFactory(title="technology")
        
    def test_get_all_category(self):
        response = self.client.get(
            reverse("category-list", kwargs={"version": "v1"})
        )
        print(f"Response data: {response.content}") 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()[0]["title"], 
            self.category.title
        )

    def test_create_category(self):
        data = {"title": "food"}
        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=data,
            format="json",
        )
        if response.status_code != status.HTTP_201_CREATED:
            print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)