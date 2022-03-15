from rest_framework import serializers
from dataclasses import fields
from apis.Product.models import Product
from apis.data.api.serializers import CategorySerializers


class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializers(many=True)
    class Meta:
        model = Product
        fields = [
            'pk',
            'name',
            'category',
            'created',
            'updated'
            ]

class ProductRegisterSerializer(serializers.ModelSerializer):
    category = CategorySerializers(many=True)
    class Meta:
        model = Product
        fields = [
            'pk',
            'name',
            'content',
            'category',
            'created',
            'updated'
            ]
    def create(self, validated_data):
        user_obj = Product(
            name=validated_data.get('name'),       
            content=validated_data.get('content'),       
            category=validated_data.get('category'),
        )
        # user_obj.set_password(validated_data.get('password'))
        user_obj.isActivated = True
        user_obj.save()
        return user_obj