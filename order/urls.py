from django.urls import path, include
from rest_framework import routers
from .views import OrderViewSet
from utils.constants import api_versions

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, 'orders')

urlpatterns = [
  path(api_versions['v1'], include(router.urls))
]