from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()
  permission_classes = [IsAuthenticated]
