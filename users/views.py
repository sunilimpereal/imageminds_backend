from cgitb import reset
from datetime import datetime
import optparse
from urllib import response
from grades.models import Grade
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

import jwt
import datetime

from .helpers import send_otp_to_phone


from .serializers import StudentSerializer, UserSerializer
from .models import Student, User

# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        logedIn = False
        student = Student.objects.filter(email=email).first()
        if student is None:
            raise AuthenticationFailed('Student not found')
        if not student.password == password:
            raise AuthenticationFailed('Incorrect Password')
        if student.loggedIn is True:
            raise AuthenticationFailed('Already Logged In ')
        else:
           data = {"loggedIn": True}
           serialist = StudentSerializer(student,data=data,partial=True)
           if serialist.is_valid():
               serialist.save()
               
        payload = {
            'id':student.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=600),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload,'secret',algorithm='HS256').decode('utf-8')
        response = Response()
        response.set_cookie(key='jwt',value=token)
        response.data = StudentSerializer(student).data
        # response.data = {
        #     'id': student.id,
        #     'email': student.email,
        #     'name':student.username,
        #     'jwt':token,
        #     'loggedIn': student.loggedIn,
        # }
        return response
    
class LoginOTPVerifyView(APIView):
    def post(self,request):
        mobile = request.data['mobile']
        otp = request.data['otp']
        logedIn = False
        student = Student.objects.filter(mobile=mobile).first()
        if student is None:
            raise AuthenticationFailed('Student not found')
        if not student.otp == otp:
            raise AuthenticationFailed('Incorrect otp')
        if student.loggedIn is True:
            raise AuthenticationFailed('Already Logged In ')
        else:
           data = {"loggedIn": True}
           serialist = StudentSerializer(student,data=data,partial=True)
           if serialist.is_valid():
               serialist.save()
               
        payload = {
            'id':student.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=600),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload,'secret',algorithm='HS256').decode('utf-8')
        response = Response()
        response.set_cookie(key='jwt',value=token)
        response.data = StudentSerializer(student).data

        return response   
    
class LoginMobSendOTPView(APIView):
    def post(self,request):
        mobile = request.data['mobile']
        logedIn = False
        student = Student.objects.filter(mobile=mobile).first()
        if student is None:
            raise AuthenticationFailed('Student not found')
        if student.loggedIn is True:
            raise AuthenticationFailed('Already Logged In ')
        else:
            otp = send_otp_to_phone(student.mobile,student.username)
            if otp is None:
                raise AuthenticationFailed('Failed to send OTP')
            data = {"otp": otp}
            serialist = StudentSerializer(student,data=data,partial=True)
            if serialist.is_valid():
               serialist.save()
        
        response = Response()
        response.data = StudentSerializer(student).data
        return response

    
class LogoutView(APIView):
    def post(self,request):
        email = request.data['email']
        student = Student.objects.filter(email=email).first()
        if student is None:
            raise AuthenticationFailed('User not found')
        if student.loggedIn is True:
            data = {"loggedIn": False}
            serialist = UserSerializer(student,data=data,partial=True)
            if serialist.is_valid():
               serialist.save()
            response = Response()
            response.data = {
            'email':student.email,
            'message': "Successfully Logged Out" 
            }
            return response
        else:
           raise AuthenticationFailed('Error Logging out')




## students
class RegisterStudentView(APIView):
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    
    def get(self,request):
        uid = self.request.query_params.get('uid')
        students = Student.objects.filter(userCode = uid)
        serializer= StudentSerializer(students,many =True)
        return Response(serializer.data)