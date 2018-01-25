#!/usr/bin/env python
"""
Base student model
"""
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.dispatch import receiver


class Student(models.Model):
    """Student's model."""
    login = models.CharField(
        max_length=20,
        blank=False,
        help_text='Intra login'
    )



    def __str__(self):
        return '{} - {}'.format(self.login, self.id)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Post create hook."""
    if created:
        Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    """Post save hook."""
    instance.student.save()
