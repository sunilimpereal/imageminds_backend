from cgitb import reset
from datetime import datetime
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

import jwt
import datetime


from .serializers import UserSerializer
from .models import User

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
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        if user.loggedIn is True:
            raise AuthenticationFailed('Already Logged In ')
        else:
           data = {"loggedIn": True}
           serialist = UserSerializer(user,data=data,partial=True)
           if serialist.is_valid():
               serialist.save()
               
        payload = {
            'id':user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=600),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload,'secret',algorithm='HS256').decode('utf-8')
        response = Response()
        response.set_cookie(key='jwt',value=token)
        response.data = {
            'jwt':token,
            'loggedIn': user.loggedIn 
        }
        return response
    
class UserView(APIView):
    def get(self,request):
        token = request.COOKIES.GET('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token,'secret',algorithm=['HS26'])
        except:
            raise AuthenticationFailed('Expired')
        user = User.objects.filter(id = payload['id']).first()
        serializer= UserSerializer(user)
        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self,request):
        email = request.data['email']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        if user.loggedIn is True:
            data = {"loggedIn": False}
            serialist = UserSerializer(user,data=data,partial=True)
            if serialist.is_valid():
               serialist.save()
            response = Response()
            response.data = {
            'email':user.email,
            'message': "Successfully Logged Out" 
            }
            return response
        else:
           raise AuthenticationFailed('Error Logging out')