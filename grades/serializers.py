from rest_framework import serializers
from .models import Grade, Video


class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ['name', 'grade', 'couseName']


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ['name', 'fileName', 'grade']
