import email
from django.db import models
from django.contrib.auth.models import AbstractUser

from grades.models import Grade

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=25, unique=True)
    mobile = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=255)
    loggedIn = models.BooleanField(default=False)
    otp = models.IntegerField(default=9898)
    username = models.CharField('username', max_length=150, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


class Student(models.Model):

    # new data fields
    userCode        = models.CharField(max_length=15,unique=True)
    username        = models.CharField('username', max_length=150, unique=True)
    password        = models.CharField(max_length=50)
    firstName       = models.CharField(max_length=150)
    lastName        = models.CharField(max_length=150)
    dob             = models.DateField()
    gender          = models.CharField(max_length=15)
    schoolName      = models.CharField(max_length=250)
    grade           = models.ManyToManyField(Grade)
    medium          = models.CharField(max_length=50)
    city            = models.CharField(max_length=250)
    fatherName      = models.CharField(max_length=150)
    motherName      = models.CharField(max_length=150)
    email           = models.CharField(max_length=100, unique=True)
    emailAlt        = models.CharField(max_length=100)
    mobile          = models.CharField(max_length=12, unique=True)
    mobileAlt       = models.CharField(max_length=12)
    address         = models.CharField(max_length=250)
    area            = models.CharField(max_length=250)
    city            = models.CharField(max_length=250)
    state           = models.CharField(max_length=250)
    zipcode         = models.CharField(max_length=8)
    country         = models.CharField(max_length=250)
    loggedIn        = models.BooleanField(default=False)
    otp             = models.IntegerField(default=9898)
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.userCode