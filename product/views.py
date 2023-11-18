from rest_framework import viewsets, permissions
from .models import Product
from .serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
