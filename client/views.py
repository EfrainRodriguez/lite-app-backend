from rest_framework import viewsets
from .models import Client
from .serializer import ClientSerializer

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
  serializer_class = ClientSerializer
  queryset = Client.objects.all()