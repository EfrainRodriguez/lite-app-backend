from rest_framework import viewsets
from .models import Client
from .serializer import ClientSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
  serializer_class = ClientSerializer
  queryset = Client.objects.all()
  permission_classes = [IsAuthenticated]
