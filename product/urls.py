from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet
from utils.constants import api_versions

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, 'products')

urlpatterns = [
  path(api_versions['v1'], include(router.urls))
]