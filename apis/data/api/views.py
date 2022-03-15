import pdb
from django.shortcuts import render,HttpResponse
# from ..models import ProductSite
from .serializers import *
# from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import generics
from http import HTTPStatus

# class ProductDataApiView(generics.RetrieveAPIView):

#     # permissions_classes = [permissions.IsAuthenticated]
#     # authentication_classes = [JSONWebTokenAuthentication]
#     # serializer_class = ProductSiteSerializers
#     # queryset = ProductSite.objects.all()

#     import pdb
#     def get(self, request, pk, *args, **kwargs):
#         # logger.info(f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n Retrieving details for qualiID = {pk}\n\n ")
#         # try:
#             # pdb.set_trace()
#             print(pk)
#             model =  Comment.objects.get(pk=pk)
#             serializer = CommentSerializers(model)
#             print(serializer.data)
          
#             response = {
#                 'success': True,
#                 'status_code':  HTTPStatus.OK,
#                 'message': 'Qualification data fetched successfully',
#                 'data': serializer.data
#             }
#             print(f"Exit log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {response}\n\n")
#         # except Exception as e:
#         #     response = {
#         #         'success': False,
#         #         'status_code': HTTPStatus.BAD_REQUEST,
#         #         'message': 'Qualification Details does not exists',
#         #         'error': str(e)
#         #     }
#             # print(f"Exit log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n  {str(e)}")
#             return Response(response)

# class ProductDataApiRegister(generics.CreateAPIView):
#     # permissions_classes = [permissions.IsAuthenticated]
#     # authentication_classes = [JSONWebTokenAuthentication]
#     # queryset = Qualification.objects.all()
#     # serializer_class = QualificationSerializer

#     def post(self, request, *args, **kwargs):
#         # logger.info(f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n Entered data:{request.data}\n\n")
#         try:
#             depart_obj = self.create(request, *args, **kwargs)
#             status_code = HTTPStatus.OK
#             response = {
#                 'success':True,
#                 'status_code': status_code,
#                 'message': "Qualification added successfully.",
#                 'data': request.data
#             }
#             # logger.info(f"Exit log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {response}\n\n")
#         except Exception as e:
#             status_code = HTTPStatus.BAD_REQUEST
#             response = {
#                 'success':False,
#                 'status_code': status_code,
#                 'message': "Please, enter valid data.",
#                 'error':str(e)
#             }
#             # logger.error(f"Exit log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n  {str(e)}")
#         return Response(response, status=status_code)