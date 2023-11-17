from django.db import models

# Create your models here.
class Order(models.Model):
  client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
  products = models.ManyToManyField('product.Product')
  total = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  class Meta:
    verbose_name = "Order"
    verbose_name_plural = "Orders"
    ordering = ['-created_at']
  def __str__(self):
    return self.client.name
