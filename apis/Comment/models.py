from distutils.command.build_py import build_py
from django.db import models
from apis.Product.models import Product
from apis.account.models import UserDetail
# Create your models here.

class Comment(models.Model):
    comment         = models.TextField(max_length=255)
    user_id         = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    created         = models.DateField(auto_now_add=True)
    updated         = models.DateField(auto_now=True)
    isDeleted       = models.BooleanField(default = False,null=True)

    def __str__(self):
        return self.comment