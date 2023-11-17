from django.urls import path, include
from rest_framework import routers
from .views import ClientViewSet
from utils.constants import api_versions

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet, 'clients')

urlpatterns = [
  path(api_versions['v1'], include(router.urls))
]