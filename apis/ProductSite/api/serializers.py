from rest_framework import serializers
from dataclasses import fields
from apis.ProductSite.api.serializers import ProductSite
from apis.Product.api.serializers import ProductSerializers
from apis.data.api.serializers import CompanySerializers,ProductSizeSerializers

class ProductSiteSerializers(serializers.ModelSerializer):
    product = ProductSerializers()
    company = CompanySerializers()
    productsize = ProductSizeSerializers()
    class Meta:
        model = ProductSite
        fields = [
            'name',
            'product',
            'url',
            'price',
            'company',
            'productsize',
            'created',
            'updated'
        ]