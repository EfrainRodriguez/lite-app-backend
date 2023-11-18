from rest_framework import viewsets
from .models import Order
from .serializer import OrderSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer
  permission_classes = [IsAuthenticated]
