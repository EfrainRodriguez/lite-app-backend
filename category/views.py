from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()
