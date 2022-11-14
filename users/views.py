from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .schema import response_schema_dict_logout,response_schema_dict_create,response_schema_dict_login
from .serializer import UserSerializer
from .models import User

# Create your views here.


# Create New User
@swagger_auto_schema(methods=['POST'], tags=['SIGN UP'], request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='tempUser'),
        'email': openapi.Schema(type=openapi.FORMAT_EMAIL, description='temp@tempmail.com'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='tempPassword'),
    }),responses=response_schema_dict_create)
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def AddUser(request):
    try:
        check = User.objects.filter(email=request.data['email'])
        if check:
            raise TypeError("Email already exists")
        serializer = UserSerializer(data=request.data)
        print(serializer.is_valid)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'User Created Successfuly',
                'success': True
            }, status=HTTP_200_OK)
        else:
            raise ValueError("Something Went Wrong")
    except Exception as error:
        print(error)
        return Response({
            'message': str(error),
            'success': False
        }, status=HTTP_400_BAD_REQUEST)


# User Login
@swagger_auto_schema(methods=['POST'], tags=['SIGN IN'], request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.FORMAT_EMAIL, description='temp@tempmail.com'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='tempPassword'),
    }),responses=response_schema_dict_login)
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def Login(request):
    try:
        check = User.objects.get(email=request.data['email']).check_password(
            request.data['password'])
        if check:
            authenticate(
                request, email=request.data['email'], password=request.data['password'])
            user = User.objects.get(email=request.data['email'])
            login(request, user)
            token = Token.objects.filter(user_id=user.pk)
            if not token:
                token = Token.objects.create(user_id=user.pk)
            else:
                token = token[0]
            return Response({
                'success': True,
                'data': {'token': token.key, 'name': user.get_username()},
            }, status=HTTP_200_OK)
        else:
            return Response({
                'message': 'Invalid Username or Password',
                'success': False
            }, status=HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({
            'message': 'User not found !',
            'success': False
        }, status=HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({
            'message': str(error),
            'success': False
        }, status=HTTP_400_BAD_REQUEST)


# User Logout
@swagger_auto_schema(methods=['GET'], tags=['SIGN OUT'],responses=response_schema_dict_logout)
@api_view(['GET'])
def Logout(request):
    try:
        request.user.auth_token.delete()
        logout(request=request)
        return Response({
            'success': True,
            'message': 'Logged out successfully !',
        }, status=HTTP_200_OK)

    except Exception as error:
        print(error)
        return Response({
            'message': str(error),
            'success': False
        }, status=HTTP_400_BAD_REQUEST)
