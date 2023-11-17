from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewSet
from utils.constants import api_versions

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet, 'companies')

urlpatterns = [
  path(api_versions['v1'], include(router.urls))
]