from django.urls import path,path
from apis.account.api.views import (ForgotPasswordVerifyOTP,
                                    ChangePasswordView,
                                    UserLoginApi,
                                    AccountDataApiView,
                                    UserRegisterApi,
                                    UserListApi,
                                    UserUpdateApi,
                                    UserDeleteApi ,
                                    ValidateEmailSendOTP,
                                    ValidateOTP,
                                    ForgotPasswordSendOTP,
                                    LoginValidateOTP,
                                    LogInEmailSendOTP)
from apis.data.api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', UserRegisterApi.as_view()),
    path('details/', UserListApi.as_view()),
    path('<int:pk>', AccountDataApiView.as_view(), name='home'),
    path('update/<int:pk>/', UserUpdateApi.as_view()),
    path('delete/<int:pk>/', UserDeleteApi.as_view()),

    path('email_verify_send_otp/', ValidateEmailSendOTP.as_view()),
    path('email_varify_otp/', ValidateOTP.as_view()),

    path('forgot_password_send_otp/', ForgotPasswordSendOTP.as_view()),
    path('forgot_password_varify_otp/', ForgotPasswordVerifyOTP.as_view()),
    path('change_password/', ChangePasswordView.as_view()),

    path('login_send_otp/', LogInEmailSendOTP.as_view()),
    path('login_varify_otp/', LoginValidateOTP.as_view()),
    path('login/', UserLoginApi.as_view()),

    path('api/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)