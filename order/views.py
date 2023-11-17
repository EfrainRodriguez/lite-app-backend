from rest_framework import viewsets
from .models import Order
from .serializer import OrderSerializer

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer