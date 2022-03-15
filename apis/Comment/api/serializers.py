from dataclasses import fields
from rest_framework import serializers
from apis.Comment.models import Comment
from apis.Product.api.serializers import ProductSerializers

class CommentSerializers(serializers.ModelSerializer):
    product = ProductSerializers()
    # user = UserSerializers()
    class Meta:
        model = Comment
        fields = [
            'title',
            'content',
            'product',
            'user',
            'created',
            'updated'
            ]

class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'title',
            'content',
            'product',
            'user',
        ]

    def create(self, validated_data):
        
        user_obj = Comment(
            title=validated_data.get('title'),
            content=validated_data.get('content'),
            product=validated_data.get('product'),
            user=validated_data.get('user'),            
        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.isActivated = True
        user_obj.save()
        return user_obj
