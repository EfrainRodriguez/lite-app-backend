from django.db import models

# Create your models here.
class Company(models.Model):
    nit = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ['-created_at']
    def __str__(self):
        return self.name