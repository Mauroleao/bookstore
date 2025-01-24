from django.urls import path, include
from rest_framework import routers

from order import viewsets

router = routers.SimpleRouterRouter()
router.register(r'product', viewsets.OrderViewSet, basename='product')

urlpattern = [
    path('', include(router.urls))
]