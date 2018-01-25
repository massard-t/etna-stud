#!/usr/bin/env python
"""
"""
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from etnadust.models import Student


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """API-available attributes"""
        model = Group
        fields = (
            'url',
            'name',
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        """API-available attributes"""
        model = User
        fields = (
            'url',
            'username',
            'email',
            'groups',
            'is_staff',
            'is_active',
            'is_superuser',
        )


class StudentSerializer(serializers.ModelSerializer):
    """No modification required"""
    user = UserSerializer
    class Meta:
        """API-available attributes"""
        model = Student
        fields = (
            'id',
            'url',
            'login',
        )
