from email.policy import default
import pdb
import smtplib,ssl
import random
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics, permissions
from http import HTTPStatus
from apis.account.models import UserDetail,EmailOTP
from .serializers import UserDeteilSerializers, UserUpdateSertializer,UserChangePasswordSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from ..models import UserDetail
from django.db.models import Q
# from ..models import ProductSite
# from rest_framework.renderers import JSONRenderer
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import datetime
import jwt

#FOR USER REGISTER
class UserRegisterApi(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [JSONWebTokenAuthentication]
    queryset = UserDetail.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            import pdb
            # pdb.set_trace()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # print(request.data.userID)
            serializer.save()
            # payload = {
            # 'id': serializer.data,
            # 'int': str(datetime.datetime.utcnow()),
            # 'exp': str(datetime.datetime.utcnow() + datetime.timedelta(minutes=1)),
            # }
            # token = jwt.encode(payload, 'secret',
            #                     algorithm='HS256').decode('utf-8')

            # response = Response()
            # response.set_cookie(key='jwt', value=token, httponly=True)

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


class AddCommentsApi(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = AddCommentserializers

    def post(self, request, *args, **kwargs):

        import pdb
        # pdb.set_trace()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(request.data.userID)
        serializer.save()

        status_code = HTTPStatus.OK 
        response = {
            'status': True,
            'status_code': status_code,
            'message': 'comment add successfully.',
            'data': {
                'user': serializer.data,
                'token': 'token',
            }
        }
        return Response(response, status=status_code)


class UserCommentAPI(generics.ListAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentDataserializers

    def get(self, request, pk):

        comment_obj = Comment.objects.filter(user = pk)
        serializer = CommentDataserializers(comment_obj, many=True)

        user_obj = UserDetail.objects.get(pk=pk)
        userserializer = UserDeteilSerializers(user_obj)

        status_code = HTTPStatus.OK
        if user_obj.isDeleted == False:
            response = {
                'success': True,
                'status_code': status_code,
                'message': 'Comment Data fetched successfully',
                'data': {"user":userserializer.data,
                    "comments":serializer.data}
            }
        else:
            status_code = HTTPStatus.BAD_REQUEST
            response = {
                'success': False,
                'status_code': status_code,
                'message': 'Enter a Velid Data',
                'data': "User Not Found"
            }
        return Response(response, status=status_code)

#FOR USER LOGIN 
class UserLoginApi(APIView):
    def post(self, request):
        # pdb.set_trace()
        try:
            email = request.data["email"]
            password = request.data["password"]

            user = UserDetail.objects.filter(
                Q(email__iexact=email) | Q(username__iexact=email))
            if user.count() != 1:
                raise AuthenticationFailed("User not found")

            user = user.first()
            if not user.check_password(password):
                raise AuthenticationFailed("Inccorect Password")

            obj = UserDetail.objects.get(userID=user.userID)
            serializer = UserDeteilSerializers(obj)

            payload = {
                'id': user.userID,
                'exp': str(datetime.datetime.utcnow() + datetime.timedelta(minutes=1)),
                'int': str(datetime.datetime.utcnow()),
            }
            token = jwt.encode(payload, 'secret',
                               algorithm='HS256').decode('utf-8')

            response = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)

            status_code = HTTPStatus.OK
            response.data = {
                'success': True,
                'status_code': status_code,
                'message': 'User Logged In successfully.',
                'data': {
                    'user': serializer.data,
                    'token': token,
                }
            }
        except Exception as e:
            status_code = HTTPStatus.BAD_REQUEST
            response = {
                'success': True,
                'status_code': status_code,
                'message': 'Please, enter valid data.',
                'data': {
                    'user': str(e),
                }
            }
            return Response(response)
        return response

# SHOW ALL USER DATA IN DATABASE
class UserListApi(generics.ListAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]
    queryset = UserDetail.objects.all()
    serializer_class = UserDeteilSerializers

    def get(self, request):

        model = UserDetail.objects.filter()
        serializer = UserDeteilSerializers(model, many=True)
        status_code = HTTPStatus.OK
        response = {
            'success': True,
            'status_code': status_code,
            'message': 'User Data fetched successfully',
            'data': serializer.data
        }
        return Response(response, status=status_code)

# THIS CLASS FOR USER UPDATE DETAILS
class UserUpdateApi(generics.UpdateAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]
    queryset = UserDetail.objects.all()
    serializer_class = UserUpdateSertializer

    def put(self, request, pk):
        try:
            model = UserDetail.objects.get(userID=pk)
            user = model
            if model.isDeleted == False:
                model = UserDetail.objects.get(userID=pk)
                serializer = UserUpdateSertializer(model, data=request.data)
                if serializer.is_valid() == True:

                    # payload = jwt_payload_handler(user)
                    # token = jwt_encode_handler(payload)
                    # user.token = token

                    user.save()
                    serializer.save()
                    serializer1 = UserUpdateSertializer(model)
                    status_code = HTTPStatus.OK
                    response = {
                        'success': True,
                        'status_code':  status_code,
                        'message': 'User Data Updated Successfully',
                        'data': serializer1.data
                    }
                else:
                    status_code = HTTPStatus.OK
                    response = {
                        'success': False,
                        'status_code': HTTPStatus.BAD_REQUEST,
                        'message': 'Your entered data is already exist',
                    }
            else:
                status_code = HTTPStatus.OK
                response = {
                    'success': False,
                    'status_code': HTTPStatus.BAD_REQUEST,
                    'message': 'User details does not exists',
                }
        except Exception as e:
            status_code = HTTPStatus.OK
            response = {
                'success': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'something is wrong',
                'error': str(e)
            }
        return Response(response, status=status_code)

# SHOW USER DETAILS
class AccountDataApiView(generics.RetrieveAPIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            # pdb.set_trace()
            print(pk)
            user_obj = UserDetail.objects.get(pk=pk, isDeleted=False)
            serializer = UserDeteilSerializers(user_obj)

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

# USER DELETE 
class UserDeleteApi(generics.DestroyAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDeteilSerializers

    def delete(self, request, pk):
        # try:
            model = UserDetail.objects.get(userID=pk)
            comment_obj = Comment.objects.filter(user = pk)
            if not model:
                status_code = HTTPStatus.NOT_FOUND
                response = {
                    'success': False,
                    "message": "User Not Found",
                    "status_code": status_code,
                }
            else:
                model.isDeleted = True
                model.save()              
                
                # for object in comment_obj:
                #     comment_obj.isDeleted == True
                #     object.save()
                
                for comment in comment_obj:
                    comment.isDeleted = True
                    comment.save()
                status_code = HTTPStatus.OK
                response = {
                    'success': True,
                    "message": "User Data Deleted Successfully.",
                    "status_code": status_code,
                }
        # except Exception as e:
        #     status_code = HTTPStatus.OK
        #     response = {
        #         'success': False,
        #         "message": "User Not Found",
        #         "status_code": HTTPStatus.BAD_REQUEST,
        #         "error": str(e)
        #     }
            return Response(response, status_code)

#CHANGE PASSWORD 
class ChangePasswordView(APIView):
    permission_classes = [permissions.AllowAny]
    queryset = UserDetail.objects.all()
    serializer_class = UserChangePasswordSerializer

    def put(self, request):
        # import pdb
        # pdb.set_trace()
        email = request.data.get('email')
        user = UserDetail.objects.get(email=email)
        # EmailOTP.objects.get(email=email).delete()
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user.set_password(serializer.data.get('password'))
            user.save()
            status_code = HTTPStatus.OK
            response = {
                'status': True,
                'status_code': status_code,
                'message': 'Password update successfully.'
            }
            return Response(response, status=status_code)
        else :
            status_code = HTTPStatus.BAD_REQUEST
            response = {
                'status': False,
                'status_code': "400",
                'message': 'Password update successfully.'
            }
            return Response(response,status=status_code)

# GENRTE OTP
def OtpSend(email_otp):
    if email_otp:
        OTP = str(random.randint(11111, 999999))
        return OTP
    else :
        return False

# SEAND EMAIL
def email_send(email,message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "pratik138.rejoice@gmail.com"   # Enter your address
    receiver_email = email  # Enter receiver address
    password = "pratik@0011"
    # otp = 343434

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# EMIAL VERIFY AND SEND OTP
class ValidateEmailSendOTP(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        email_otp = request.data.get('email')  
        key = OtpSend(email_otp)
        if key:
            old = EmailOTP.objects.filter(email__iexact=email_otp)
            if old.exists():
                old = old.first()
                count = old.count
                if count > 10:
                    status_code = HTTPStatus.OK
                    response = {
                        'status': False,
                        'status_code': HTTPStatus.UNAUTHORIZED,
                        'message': 'sending otp limit exceeded.'
                    }
                    return Response(response, status=status_code)
                old.count = count + 1
                old.otp = key
                old.save()
            else:
                old = EmailOTP.objects.create(
                    email=email_otp,
                    otp=key,
                )
            message = f"""
                        Verify Email Address

                        Verify OTP is : {key}."""
            email_send(old.email, message)
            status_code = HTTPStatus.OK
            response = {
                'status': True,
                'status_code': HTTPStatus.OK,
                'message': 'OTP sent successfully.'
            }
            return Response(response, status_code)
        else:
            status_code = HTTPStatus.OK
            response = {
                'status': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'Sending otp error.'
            }
            return Response(response, status=status_code)

# OR OTP
class ValidateOTP(APIView):

    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', False)
        otp_sent = request.data.get('otp',  False)
        default_otp = None
        if email and otp_sent:
            old = EmailOTP.objects.filter(email__iexact=email)
            if old.exists():
                old = old.first()
                otp = old.otp
                if str(otp_sent) == str(otp):
                    old.validated = True
                    old.save()
                    status_code = HTTPStatus.OK
                    response = {
                        'status': True,
                        'status_code': HTTPStatus.ACCEPTED,
                        'message': 'OTP Verify',
                    }
                    old.otp = default_otp
                    old.save()
                    return Response(response, status=status_code)
                else:
                    status_code = HTTPStatus.OK
                    response = {
                        'status': False,
                        'status_code': HTTPStatus.UNAUTHORIZED,
                        'message': 'Please enter a valid OTP',
                    }
                    return Response(response, status=status_code)
            else:
                status_code = HTTPStatus.OK
                response = {
                    'status': False,
                    'status_code': HTTPStatus.BAD_REQUEST,
                    'message': 'Frist Send OTP ',
                }
                return Response(response, status=status_code)
        else:
            status_code = HTTPStatus.OK
            response = {
                'status': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'Please enter a valid OTP',
            }
            # logger.error(f"Exit log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n  {str(e)}")
            return Response(response, status_code)

#FORGATE PASSWORD VERIFY EMAIL AND OTP
class ForgotPasswordSendOTP(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        
        email_otp = request.data.get('email')
        if email_otp:
            user = UserDetail.objects.filter(email__iexact=email_otp)
            if user.exists():
                key = OtpSend(email_otp)
                if key:
                    old = EmailOTP.objects.filter(email__iexact=email_otp)
                    if old.exists():
                        old = old.first()
                        count = old.count
                        if count > 50:
                            status_code = HTTPStatus.OK
                            response = {
                                'status': False,
                                'status_code': HTTPStatus.UNAUTHORIZED,
                                'message': 'sending otp limit exceeded.'
                            }
                            return Response(response, status=status_code)
                        old.count = count + 1
                        old.otp = key
                        old.save()
                    else:
                        old = EmailOTP.objects.create(
                            email=email_otp,
                            otp=key,
                        )
                    message = f"""
                                Forgot Password

                                Forgot Password OTP is : {key}."""
                    email_send(old.email, message)
                    status_code = HTTPStatus.OK
                    response = {
                        'status': True,
                        'status_code': HTTPStatus.OK,
                        'message': 'OTP sent successfully.'
                    }
                    return Response(response, status=status_code)
                else:
                    status_code = HTTPStatus.OK
                    response = {
                        'status': False,
                        'status_code': HTTPStatus.BAD_REQUEST,
                        'message': 'Sending otp error.'
                    }
                    return Response(response, status=status_code)
            else:
                status_code = HTTPStatus.OK
                response = {
                    'status': False,
                    'status_code': HTTPStatus.BAD_REQUEST,
                    'message': 'Email Address does not exists.Please go for registration process.'
                }
                return Response(response, status=status_code)
        else:
            status_code = HTTPStatus.OK
            response = {
                'status': False,
                'status_code': HTTPStatus.NOT_FOUND,
                'message': 'Email address is not given.'
            }
            # logger.error(f"Exit log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n  {str(e)}")
            return Response(response, status=status_code)

# VERIFY OTP FOR FORGATE PASSWORD
class ForgotPasswordVerifyOTP(APIView):

    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', False)
        otp_sent = request.data.get('otp',  False)

        if email and otp_sent:
            old = EmailOTP.objects.filter(email__iexact=email)
            if old.exists():
                old = old.first()
                otp = old.otp
                if str(otp_sent) == str(otp):
                    old.validated = True
                    old.save()
                    status_code = HTTPStatus.OK
                    response = {
                        'status': True,
                        'status_code': HTTPStatus.ACCEPTED,
                        'message': 'OTP matched, please proceed for forgot password.',
                    }
                    old.otp = None
                    old.save()
                    return Response(response, status=status_code)
                else:
                    status_code = HTTPStatus.OK
                    response = {
                        'status': False,
                        'status_code': HTTPStatus.UNAUTHORIZED,
                        'message': 'OTP incorect',
                    }
                    return Response(response, status=status_code)
            else:
                status_code = HTTPStatus.OK
                response = {
                    'status': False,
                    'status_code': HTTPStatus.BAD_REQUEST,
                    'message': 'First proceed via sending OTP request',
                }
                return Response(response, status=status_code)
        else:
            status_code = HTTPStatus.OK
            response = {
                'status': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'Please provide both email and otp for validation',
            }
            # logger.error(f"Exit log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n  {str(e)}")
            return Response(response, status_code)

# USER LOGIN VERIFY EMAIL 
class LogInEmailSendOTP(APIView):
    ermission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email_otp = request.data.get('email')  
        key = OtpSend(email_otp)
        if key:
            old = EmailOTP.objects.filter(email__iexact=email_otp)
            if old.exists():
                old = old.first()
                count = old.count
                if count > 10:
                    status_code = HTTPStatus.OK
                    response = {
                        'status': False,
                        'status_code': HTTPStatus.UNAUTHORIZED,
                        'message': 'sending otp limit exceeded.'
                    }
                    return Response(response, status=status_code)
                old.count = count + 1
                old.otp = key
                old.save()
            else:
                old = EmailOTP.objects.create(
                    email=email_otp,
                    otp=key,
                )
            message = f"""
            Subject: Login

            login otp is : {key}."""
            email_send(old.email, message)
            status_code = HTTPStatus.OK
            response = {
                'status': True,
                'status_code': HTTPStatus.OK,
                'message': 'OTP sent successfully.'
            }
            return Response(response, status_code)
        else:
            status_code = HTTPStatus.OK
            response = {
                'status': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'Sending otp error.'
            }
            return Response(response, status=status_code)

#LOGIN VERIFY OTP
class LoginValidateOTP(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', False)
        otp_sent = request.data.get('otp',  False)

        default_otp = None

        if email and otp_sent:
            old = EmailOTP.objects.filter(email__iexact=email)
            user_name = UserDeteilSerializers
            if old.exists():
                old = old.first()
                otp = old.otp
                if str(otp_sent) == str(otp):
                    old.validated = True
                    old.save()
                    status_code = HTTPStatus.OK
                    response = {
                        'status': True,
                        'status_code': HTTPStatus.ACCEPTED,
                        'message': 'OTP Verify, Welcome Back ',
                    }
                    old.otp = default_otp
                    old.save()
                    return Response(response, status=status_code)
                else:
                    status_code = HTTPStatus.OK
                    response = {
                        'status': False,
                        'status_code': HTTPStatus.UNAUTHORIZED,
                        'message': 'Please enter a valid OTP',
                    }
                    return Response(response, status=status_code)
            else:
                status_code = HTTPStatus.OK
                response = {
                    'status': False,
                    'status_code': HTTPStatus.BAD_REQUEST,
                    'message': 'Frist Send OTP ',
                }
                return Response(response, status=status_code)
        else:
            status_code = HTTPStatus.OK
            response = {
                'status': False,
                'status_code': HTTPStatus.BAD_REQUEST,
                'message': 'Please enter a valid OTP',
            }
            return Response(response, status_code)


class TagDataApi(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    queryset = tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request, pk):
        try:
            tag_obj = tag.objects.filter(id = pk)
            serializer = TagSerializer(tag_obj, many=True)
            if tag_obj:
                status_code = HTTPStatus.OK
                response = {
                    'success': True,
                    'status_code': status_code,
                    'message': 'Tag Data fetched successfully',
                    'data': serializer.data
                    }
            else:
                status_code = HTTPStatus.BAD_REQUEST
                response = {
                    'success': False,
                    'status_code': status_code,
                    'message': 'Enter a Velid Data',
                    'data': "User Not Found"
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


class AddTagApi(generics.CreateAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    queryset = tag.objects.all()
    serializer_class = TagSerializer   
    def post(self, request, *args, **kwargs):

        import pdb
        # pdb.set_trace()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(request.data.userID)
        serializer.save()

        status_code = HTTPStatus.OK 
        response = {
            'status': True,
            'status_code': status_code,
            'message': 'tag add successfully.',
            'data': {
                'user': serializer.data,
                'token': 'token',
            }
        }
        return Response(response, status=status_code)

