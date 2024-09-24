from django.urls import path
from . import views
from .utils import SignUp

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('auth/', views.auth, name='auth'),
    path('guest/posts', views.getGuestUserPosts, name='guestposts'),
    path('posts', views.getUserPosts, name='posts')
]