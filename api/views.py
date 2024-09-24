from rest_framework.decorators import api_view
from .utils import *
from rest_framework import generics


@api_view(['POST', 'GET'])
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