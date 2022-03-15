import pdb
from django.shortcuts import render,HttpResponse
# from ..models import ProductSite
from .serializers import *
# from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import generics,permissions
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from http import HTTPStatus
from apis.Product.models import Product
from .serializers import ProductSerializers,ProductRegisterSerializer




class ProductDataApiView(generics.RetrieveAPIView):
     def get(self, request, pk, *args, **kwargs):
        try:
            # pdb.set_trace()
            print(pk)
            model =  Product.objects.get(pk=pk,isDeleted=False)
            serializer = ProductSerializers(model)
            # print(serializer.data)
          
            response = {
                'success': True,
                'status_code':  HTTPStatus.OK,
                'message': 'Product data fetched successfully',
                'data': serializer.data
            }
        except Exception as e:
            response = {
                'success': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'Product Details does not exists',
                'error': str(e)
            }
        return Response(response, status=HTTPStatus.OK)

class ProductRegisterApi(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [JSONWebTokenAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductRegisterSerializer

    def post(self, request, *args, **kwargs):
        # try:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # import pdb
        # pdb.set_trace()
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
                # 'user': ProductSerializers(user, context=self.get_serializer_context()).data,
                'token': 'token',
            }
        }
        # except Exception as exc:
        #     status_code = HTTPStatus.OK
        #     response = {
        #         'status': False,
        #         'status_code': HTTPStatus.BAD_REQUEST,
        #         'message': 'Please, enter valid data',
        #         'error': str(exc),
        #     }
        return Response(response, status=status_code)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}