from django.db import models
from apis.Product.models import Product
from apis.data.models import Company,ProductSize
# Create your models here.

class ProductSite(models.Model):
    name        = models.CharField(max_length=255)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    company     = models.ForeignKey(Company, on_delete=models.CASCADE)
    productsize = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    price       = models.DecimalField(max_digits=9, decimal_places=2)
    url         = models.TextField()
    created     = models.DateField(auto_now_add=True)
    updated     = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
