from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import SignUpSerializer, UserSerializer, ActivitySerializer, ProjectSerializer, ActivityImagesSerializer, WorkSerializer
from .models import AppUsers, Posts, Projects, Work
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import UntypedToken


class SignUp(APIView):

    def post(self, request):

        data = {
            'username' : request.data['username'],
            'password' : request.data['password']
        }

        serializer = SignUpSerializer(data = data)
        
        if serializer.is_valid():

            serializer.save()

            user = User.objects.filter(username = request.data['username']).first()
            user.set_password(request.data['password'])
            user.save()

            token = RefreshToken.for_user(user)

            userData = {
                'username' : request.data['username'],
                'number' : request.data['number'],
                'password' : request.data['password'],
                'token' : str(token),
                'type' : request.data['type']
            }

            modelSerializer = UserSerializer(data = userData)

            if modelSerializer.is_valid():

                modelSerializer.save()
           
                return Response({
                    'status' : True,
                    'data' : modelSerializer.data,
                    'message' : 'Account registered'
                })
            else:
           
                field_names = []

                print(modelSerializer.errors)
           
                for field_name, field_errors in modelSerializer.errors.items():
                    field_names.append(field_name)
           
                return Response({
                    'status' : status.HTTP_400_BAD_REQUEST,
                    'data' : { },
                    'message' : f'Invalid data in {field_names}'
                })
        else:
           
            field_names = []

           
            for field_name, field_errors in serializer.errors.items():
                field_names.append(field_name)
           
            return Response({
                'status' : status.HTTP_400_BAD_REQUEST,
                'data' : { },
                'message' : f'Error : {field_names}'
            })
        

def login(request):

    username = request.query_params.get('username')

    if AppUsers.objects.filter(username=username).exists() is True:
        users = AppUsers.objects.get(username=username)
        serializer = UserSerializer(instance = users, many= False)
        if(serializer.data['password'] == request.query_params.get('password')):
            return Response({
                'status' : True,
                'data' : serializer.data,
                'message' : 'User Verified'
            })
        else:
            return Response({
                'status' : True,
                'data' : { },
                'message' : 'Wrong crendential'
            })

    else:
        return Response({
            'status' : False,
            'data' : { },
            'message' : 'Email not exists'
        })
    

def guestUser(request):

    posts = Posts.objects.all()
    serializer = ActivitySerializer(posts, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })


def getPosts(request):

    posts = Posts.objects.all()
    serializer = ActivitySerializer(posts, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })


def checkUserName(request):

    username = request.query_params.get('username')

    if AppUsers.objects.filter(username=username).exists() is True:
        return Response({
            'data' : True,
            'status' : status.HTTP_201_CREATED
        })
    else:
        return Response({
            'data' : False,
            'status' : status.HTTP_201_CREATED
        })
    

def createProject(request):
    
    serializer = ProjectSerializer(data=request.data)

    name = request.data['name']

    if Projects.objects.filter(name=name).exists() is True:
        return Response({
            'data' : {},
            'status' : status.HTTP_201_CREATED,
            'message' : 'Project Exists'
        })
    else:
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : status.HTTP_201_CREATED,
                'data' : serializer.data,
                'message' : 'New Project Created'
            })
        else:
            return Response({
                'status' : status.HTTP_400_BAD_REQUEST,
                'data' : serializer.data,
                'message' : 'Project not created'
            })
        

def getProjects(request):
    
    projects = Projects.objects.all()
    serializer = ProjectSerializer(projects, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })


def uploadImage(request):

    serializer = ActivityImagesSerializer(data=request.data)

    if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : True,
                'data' : serializer.data,
                'message' : 'Image Uploaded'
            })
    else:
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Image not Uploaded'
        })


def addActivity(request):
    
    serializer = ActivitySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : status.HTTP_201_CREATED,
            'data' : serializer.data,
            'message' : 'New Project Created'
        })
    else:
        return Response({
            'status' : status.HTTP_400_BAD_REQUEST,
            'data' : serializer.data,
            'message' : 'Project not created'
        })
    

def startWork(request):
    
    serializer = WorkSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : status.HTTP_201_CREATED,
            'data' : serializer.data,
            'message' : 'Work Started'
        })
    else:
        return Response({
            'status' : status.HTTP_400_BAD_REQUEST,
            'data' : serializer.data,
            'message' : 'Work not Started'
        })
    
def endWork(request, pk):

    data = request.data
    work = Work.objects.get(id=pk)
    serializer = WorkSerializer(instance=work, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'Work updated'
        })
    else:
        print(serializer.errors)
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Work not updated'
        })
    

def updateUser(request, pk):

    data = request.data
    users = AppUsers.objects.get(id=pk)
    serializer = UserSerializer(instance=users, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'User details updated'
        })
    else:
        print(serializer.errors)
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'User details not updated'
        })
    

def getUsersList(request):

    users = AppUsers.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })