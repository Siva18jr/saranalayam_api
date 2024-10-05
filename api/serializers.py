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


class ActivitySerializer(ModelSerializer):

    class Meta:
        model = Posts
        fields = '__all__'


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Projects
        fields = '__all__'


class ActivityImagesSerializer(ModelSerializer):

    class Meta:
        model = ActivityImages
        fields = '__all__'


class WorkSerializer(ModelSerializer):

    class Meta:
        model = Work
        fields = '__all__'


class AmountSerializer(ModelSerializer):

    class Meta:
        model = Amount
        fields = '__all__'


class FoodSerializer(ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'


class DonationSerializer(ModelSerializer):

    class Meta:
        model = Donation
        fields = '__all__'