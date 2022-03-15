from django.urls import path
from .views import *

from apis.data.api import views

urlpatterns = [
    # path('register/', views.studendDataApiRegister.as_view()),
    # path('details/', QualificationList.as_view()),
    path('<int:pk>', views.ProductDataApiView.as_view(), name='home'),
    # path('delete/<int:pk>/', QualificationDelete.as_view()),
    # path('update/<int:pk>/', QualificationUpdate.as_view()),
]

