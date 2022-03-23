from dataclasses import fields
from rest_framework import serializers
from apis.Comment.models import Comment
from apis.account.api.serializers import UserDeteilSerializers

class CommentSerializers(serializers.ModelSerializer):
    # product = ProductSerializers()
    user = UserDeteilSerializers(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = [ 
            'comment',    
            'user_id',       
            # 'created',    
            # 'updated',    
            # 'isDeleted',            
            ]

class AddCommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'comment',    
            'user_id',
        ]

    def create(self, validated_data):
        
        user_obj = Comment(
            comment=validated_data.get('title'),
            user_id=validated_data.get('user_id'),          
        )
        user_obj.isActivated = True
        user_obj.save()
        return user_obj
