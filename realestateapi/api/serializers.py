from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import realestate_data,realestate_data_2


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class realestate_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = realestate_data
        fields = "__all__"

class realestate_serializer_2(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = realestate_data_2
        fields = "__all__"
        