from django.urls import path
from . import views
from .utils import SignUp

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('auth/', views.auth, name='auth'),
    path('guest/posts', views.getGuestUserPosts, name='guestposts'),
    path('posts', views.getUserPosts, name='posts'),
    path('auth/check-username', views.usernameExists, name='checkusername'),
    path('projects', views.projects, name="projects"),
    path('activity/posts', views.activities, name="activities"),
    path('activity/images', views.images, name="activityimages"),
    path('work/start', views.work, name="workstart"),
    path('work/end/<int:pk>/', views.updateWork, name="workend"),
    path('auth/user/<int:pk>/', views.users, name="users"),
    path('auth/users/', views.getUsers, name="getusers"),
    path('amount/entries/', views.amountEntries, name="amountentries"),
    path('amount/entries/<int:pk>/', views.amountEntry, name="amountentry"),
    path('activity/posts/<int:pk>/', views.activity, name="activity"),
    path('food/', views.foodData, name="food"),
    path('donation/', views.donations, name="donations"),
    path('donation/<int:pk>/', views.donation, name="donation"),
    path('work/attendance/', views.attendance, name="attendance"),
    path('projects/info/', views.projectInfo, name="projectinfo"),
    path('work/status', views.getWorkStatus, name="workstatus"),
    path('projects/info/coordinator', views.coordinatorProjects, name="coordinatorprojectinfo"),
    path('projects/info/coordinator/amount', views.getProjectAmountEntry, name="amountcoordinatorprojectinfo"),
    path('auth/users/project/coordinator', views.getUsersByProject, name="getusersbyproject"),
    path('donation/graph', views.getDonationsGraph, name="getdonationsgraph"),
    path('food/filter', views.getFoodByDate, name="filterfood"),
    path('projects/filter', views.getProjectsGraph, name="projectgraph"),
    path('food/<int:pk>/', views.food, name="updatefood"),
    path('amount/entries/download/pdf/<str:time_period>/', views.downloadAmountData, {'format_type': 'pdf'}, name='download_pdf'),
    path('amount/entries/download/excel/<str:time_period>/', views.downloadAmountData, {'format_type': 'excel'}, name='download_excel'),
    path('projects/name/info/', views.getProjectByName, name="getprojectbyname"),
    path('projects/<int:pk>/', views.project, name="project")
]