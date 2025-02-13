#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

from order.factories import OrderFactory
from product.factories import ProductFactory
from order.serializers import OrderSerializer


class TestOrderSerializer(APITestCase):
    def setUp(self):
        self.product_1 = ProductFactory()
        self.product_2 = ProductFactory()
        self.order = OrderFactory(product=(self.product_1, self.product_2))
        self.order_serializer = OrderSerializer(self.order)

    def test_order_serializer(self):
        serializer_data = self.order_serializer.data
        self.assertEqual(
            serializer_data["product"][0]["title"], self.product_1.title
        )
        self.assertEqual(
            serializer_data["product"][1]["title"], self.product_2.title
        )