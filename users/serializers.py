from requests import request
from grades.models import Grade
from rest_framework import serializers
from .models import Student, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password',
                  'loggedIn', 'username', 'mobile', 'otp']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['userCode',
                  'username',
                  'password',
                  'firstName',
                  'lastName',
                  'dob',
                  'gender',
                  'schoolName',
                  'grade',
                  'medium',
                  'city',
                  'fatherName',
                  'motherName',
                  'email',
                  'emailAlt',
                  'mobile',
                  'mobileAlt',
                  'address',
                  'area',
                  'city',
                  'state',
                  'country',
                  'zipcode',
                  'loggedIn',
                  'deviceId',
                  'otp',

                  ]
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        grades = validated_data.pop('grade', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.password = password
        instance.save()
        
        for grade in grades:
            print(grade)
            # grade_obj = Grade.objects.get(grade = grade)
            instance.grade.add(grade)
        instance.save()
        return instance
