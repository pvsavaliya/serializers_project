import pdb
from django.shortcuts import render,HttpResponse
# from ..models import ProductSite
from .serializers import *
# from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import generics,permissions
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from http import HTTPStatus
from apis.account.models import UserDetail
from .serializers import CommentSerializers


class CommentDataApiView(generics.RetrieveAPIView):
     def get(self, request, pk, *args, **kwargs):
        try:
            # pdb.set_trace()
            print(pk)
            model =  UserDetail.objects.get(pk=pk,isDeleted=False)
            serializer = CommentSerializers(model)
            # print(serializer.data)
          
            response = {
                'success': True,
                'status_code':  HTTPStatus.OK,
                'message': 'Account data fetched successfully',
                'data': serializer.data
            }
        except Exception as e:
            response = {
                'success': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'Account Details does not exists',
                'error': str(e)
            }
        return Response(response, status=HTTPStatus.OK)


class CommentRegisterApi(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [JSONWebTokenAuthentication]
    queryset = UserDetail.objects.all()
    serializer_class = AddCommentSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            # payload = jwt_payload_handler(user)
            # token = jwt_encode_handler(payload)
            # user.isVerified = True
            # user.token = token
            user.save()
            status_code = HTTPStatus.OK
            response = {
                'status': True,
                'status_code': status_code,
                'message': 'You are registered successfully.',
                'data': {
                    'user': serializer.data,
                    'token': 'token',
                }
            }
        except Exception as exc:
            status_code = HTTPStatus.OK
            response = {
                'status': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'Please, enter valid data',
                'error': str(exc),
            }
        return Response(response, status=status_code)

    # def get_serializer_context(self, *args, **kwargs):
    #     return {"request": self.request}