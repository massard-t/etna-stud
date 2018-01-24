"""Basic Student serializer."""
from rest_framework import serializers

from etnadust import models


class StudentSerializers(serializer.ModelSerializer):
    """Student."""
    queryset = models.Student.objects.all()
    fields = ('__all__')
