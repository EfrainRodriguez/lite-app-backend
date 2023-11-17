from rest_framework import serializers
from .models import Order
from product.serializer import ProductSerializer
from client.serializer import ClientSerializer

class OrderSerializer(serializers.ModelSerializer):
  products = ProductSerializer(many=True)
  client = ClientSerializer()
  class Meta:
    model = Order
    fields = '__all__'