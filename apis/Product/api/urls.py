from django.urls import path
from apis.Product.api.views import ProductDataApiView,ProductRegisterApi
# from rest_framework_jwt.views import obtain_jwt_token

from apis.data.api import views

urlpatterns = [
    path('register/', ProductRegisterApi.as_view()),
    # path('details/', UserListApi.as_view()),
    path('<int:pk>', ProductDataApiView.as_view(), name='home'),
    # path('delete/<int:pk>/', UserDeleteApi.as_view()),
    # path('update/<int:pk>/', UserUpdateApi.as_view()),
]