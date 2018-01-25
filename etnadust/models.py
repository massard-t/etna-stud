#!/usr/bin/env python
"""
Base student model
"""
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Student(models.Model):
    """Student's model."""
    login = models.CharField(
        max_length=20,
        blank=False,
        help_text='Intra login'
    )


    def __str__(self):
        return '{} - {}'.format(self.login, self.id)
