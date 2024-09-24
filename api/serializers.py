from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers

class SignUpSerializer(ModelSerializer):
   
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]


class UserSerializer(ModelSerializer):

    token = serializers.JSONField()

    class Meta:
        model = AppUsers
        fields = '__all__'


class PostsSerializer(ModelSerializer):

    class Meta:
        model = Posts
        fields = '__all__'