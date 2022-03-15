from django.urls import path
from apis.Comment.api.views import CommentRegisterApi,CommentDataApiView
# from rest_framework_jwt.views import obtain_jwt_token

from apis.data.api import views

urlpatterns = [
    path('register/', CommentRegisterApi.as_view()),
    # path('details/', UserListApi.as_view()),
    path('<int:pk>', CommentDataApiView.as_view(), name='home'),
    # path('delete/<int:pk>/', UserDeleteApi.as_view()),
    # path('update/<int:pk>/', UserUpdateApi.as_view()),
]