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
    path('activity/posts', views.addActivity, name="activity"),
    path('activity/images', views.images, name="activityimages"),
    path('work/start', views.work, name="workstart"),
    path('work/end', views.updateWork, name="workend")
]