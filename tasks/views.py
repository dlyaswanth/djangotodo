from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .schema import response_schema_dict_list,response_schema_dict_add,response_schema_dict_delete,response_schema_dict_edit
import datetime
from .models import Task
from .serializer import TaskSerializer, TaskListSerializer


notFound = "User Not Found !"
noTask = 'No Task Found !'
# Create your views here.

# Users Todo List
@swagger_auto_schema(methods=['GET'], tags=['CRUD OPERATIONS'],responses=response_schema_dict_list)
@api_view(['GET'])
def ListView(request):
    try:
        user_id = request.user.id
        if not user_id:
            raise ValueError(notFound)
        tasks = Task.objects.filter(user_id=user_id).filter(deleted_at = None)
        if not tasks:
            raise ValueError(noTask)
        response = TaskListSerializer(data=tasks, many=True)
        return Response({
            'message': 'Successfully Fetched ',
            'success': True,
            'data': response.data
        }, status=HTTP_200_OK)
    except Exception as error:
        print(error)
        return Response({
            'message': str(error),
            'success': False
        }, status=HTTP_400_BAD_REQUEST)


# Add todo
@swagger_auto_schema(methods=['POST'], tags=['CRUD OPERATIONS'],request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'description': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'completed': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='bool'),
        'start_date': openapi.Schema(type=openapi.FORMAT_DATE, description='date'),
        'end_date': openapi.Schema(type=openapi.FORMAT_DATE, description='date'),
    }),responses=response_schema_dict_add)
@api_view(['POST'])
def AddView(request):
    try:
        user_id = request.user.id
        if not user_id:
            raise ValueError(notFound)
        request.data['user'] = user_id
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'message': 'Created Successfully',
                'success': True,
            }, status=HTTP_200_OK)
        else:
            raise ValueError("Something went wrong !")
    except Exception as error:
        print(error)
        return Response({
            'message': str(error),
            'success': False
        }, status=HTTP_400_BAD_REQUEST)


# Update todo
@swagger_auto_schema(methods=['PUT'], tags=['CRUD OPERATIONS'], request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'description': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'completed': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='bool'),
        'start_date': openapi.Schema(type=openapi.FORMAT_DATE, description='date'),
        'end_date': openapi.Schema(type=openapi.FORMAT_DATE, description='date'),
    }),responses=response_schema_dict_edit)
@api_view(['PUT'])
def UpdateView(request, task_id):
    try:
        user_id = request.user.id
        if not user_id:
            raise ValueError(notFound)
        task = Task.objects.get(id=task_id, user=user_id)
        if not task:
            raise ValueError(noTask)
        Task.objects.filter(id=task_id).filter(
            user=user_id).update(**request.data)
        return Response({
            'message': 'Updated Successfully',
            'success': True,
        }, status=HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({
            'message': noTask,
            'success': False
        }, status=HTTP_403_FORBIDDEN)
    except Exception as error:
        return Response({
            'message': str(error),
            'success': False
        }, status=HTTP_400_BAD_REQUEST)


#delete todo 
@swagger_auto_schema(methods=['DELETE'], tags=['CRUD OPERATIONS'],responses=response_schema_dict_delete)
@api_view(['DELETE'])
def DeleteView(request, task_id):
    try:
        user_id = request.user.id
        if not user_id:
            raise ValueError(notFound)
        task = Task.objects.get(id=task_id, user=user_id)
        if not task:
            raise ValueError(noTask)
        Task.objects.filter(id=task_id).filter(user=user_id).update(deleted_at=datetime.datetime.now())
        return Response({
            'message': 'Updated Successfully',
            'success': True,
        }, status=HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({
            'message': noTask,
            'success': False
        }, status=HTTP_403_FORBIDDEN)
    except Exception as error:
        return Response({
            'message': str(error),
            'success': False
        }, status=HTTP_400_BAD_REQUEST)