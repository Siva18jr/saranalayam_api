from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import SignUpSerializer, UserSerializer, PostsSerializer
from .models import AppUsers, Posts
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
    serializer = PostsSerializer(posts, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })


def getPosts(request):

    # data = {'token': request.data}
    # valid_data = UntypedToken(request.data)

    # print(valid_data)

    posts = Posts.objects.all()
    serializer = PostsSerializer(posts, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })