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
def activities(request):
    
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
    

@api_view(['POST', 'GET'])
def amountEntries(request):
    
    if request.method == 'GET':
        return getAmountEntries(request)
    
    if request.method == 'POST':
        return addAmountEntry(request)
    

@api_view(['PUT'])
def amountEntry(request, pk):

    if request.method == 'PUT':
        return updateAmountEntry(request, pk)
    

@api_view(['PUT'])
def activity(request, pk):

    if request.method == 'PUT':
        return updateActivity(request, pk)
    

@api_view(['POST', 'GET'])
def foodData(request):
    
    if request.method == 'GET':
        return getFoodData(request)
    
    if request.method == 'POST':
        return addFood(request)
    

@api_view(['POST', 'GET'])
def donations(request):
    
    if request.method == 'GET':
        return getDonations(request)
    
    if request.method == 'POST':
        return addDonation(request)
    

@api_view(['PUT'])
def donation(request, pk):

    if request.method == 'PUT':
        return updateDonation(request, pk)
    

@api_view(['GET'])
def attendance(request):
    
    if request.method == 'GET':
        return getAttendance(request)
    

@api_view(['GET'])
def projectInfo(request):
    
    if request.method == 'GET':
        return getProjectInfo(request)
    

@api_view(['GET'])
def getWorkStatus(request):
    
    if request.method == 'GET':
        return checkWork(request)
    

@api_view(['GET'])
def coordinatorProjects(request):
    
    if request.method == 'GET':
        return getProjectIncharge(request)   
    

@api_view(['GET'])
def getProjectAmountEntry(request):
    
    if request.method == 'GET':
        return getProjectAmountEntries(request)
    

@api_view(['GET'])
def getUsersByType(request):
    
    if request.method == 'GET':
        return getUsersListByType(request)  
    

@api_view(['GET'])
def getDonationsGraph(request):
    
    if request.method == 'GET':
        return getDonationGraph(request)
    

@api_view(['GET'])
def getFoodByDate(request):
    
    if request.method == 'GET':
        return getFoodListByDate(request)  
    

@api_view(['GET'])
def getProjectsGraph(request):
    
    if request.method == 'GET':
        return getProjectGraph(request)