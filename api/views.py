from rest_framework.decorators import api_view
from .utils import *
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def auth(request):

    if request.method == 'GET':
        return login(request)
    

@api_view(['GET'])
def getGuestUserPosts(request):

    if request.method == 'GET':
        return guestUser(request)
    

@api_view(['GET'])
def getUserPosts(request):

    if request.method == 'GET':
        return getPosts(request)
    

@api_view(['GET'])
def usernameExists(request):

    if request.method == 'GET':
        return checkUserName(request)
    

@api_view(['POST', 'GET'])
def projects(request):

    if request.method == 'GET':
        return getProjects(request)
    
    if request.method == 'POST':
        return createProject(request)
    

@api_view(['POST'])
def activity(request):
    
    if request.method == 'POST':
        return addActivity(request)
    

@api_view(['POST'])
def images(request):
    
    if request.method == 'POST':
        return uploadImage(request)
    

@api_view(['POST', 'GET'])
def work(request):
    
    if request.method == 'POST':
        return startWork(request)
    

@api_view(['PUT'])
def updateWork(request, pk):

    if request.method == 'PUT':
        return endWork(request, pk)
    

@api_view(['PUT'])
def users(request, pk):

    if request.method == 'PUT':
        return updateUser(request, pk)
    

@api_view(['GET'])
def getUsers(request):
    
    if request.method == 'GET':
        return getUsersList(request)