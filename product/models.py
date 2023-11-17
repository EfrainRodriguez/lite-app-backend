from django.db import models
from company.models import Company
from category.models import Category

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    characteristics = models.CharField(max_length=100)
    price = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    def __str__(self):
        return self.name
