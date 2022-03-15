from dataclasses import fields
from pyexpat import model
from apis.data.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
        
class CompanySerializers(serializers.ModelSerializer):
    # category = CategorySerializers(read_only=True)
    class Meta:
        model = Company
        fields = [
            'name',
            'url',
        ]

class ProductSizeSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductSize
        fields = [
            'name',
        ]

class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'pk',
            'name',
            ]

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



# class 