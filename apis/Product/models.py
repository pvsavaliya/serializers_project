from django.db import models
from apis.data.models import Category
# Create your models here.

class Product(models.Model):
    name     = models.CharField(max_length=255)
    content  = models.TextField(max_length=255)
    category = models.ManyToManyField(Category)
    created  = models.DateField(auto_now_add=True)
    updated  = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name