from rest_framework import serializers

from .models import Product
from company.serializer import CompanySerializer
from category.serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    categories = CategorySerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'
        