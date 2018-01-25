#!/usr/bin/python
"""
Student model.
"""
from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    """Basic student model which reflects an optimized student."""

    login = model.CharField(max_length=10)
    user = models.OneToOneField(
        User
    )

