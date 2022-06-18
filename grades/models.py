from django.db import models

# Create your models here.


class Grade(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    couseName = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=100)
    fileName = models.CharField(max_length=255)
    grade = models.ForeignKey(to=Grade, on_delete=models.CASCADE)
    def __str__(self):
        return self.name