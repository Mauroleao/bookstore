from django.urls import path, include
from rest_framework import routers

from order import viewsets

router = routers.SimpleRouterRouter()
router.register(r'order', viewsets.OrderViewSet, basename='order')

urlpattern = [
    path('', include(router.urls))
]