from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  serializer_class = UserSerializer
  queryset = User.objects.all()