"""
API views based on Django Rest Framework
"""
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from etnadust.models import Student
from etnadust import serializers 

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """Allow manipulating score through the API"""
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer
