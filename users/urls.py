from django.contrib import admin
from django.urls import path,include
from .views import LoginMobSendOTPView, LoginOTPVerifyView, LogoutView, RegisterView,LoginView,UserView
urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('login_send_otp',LoginMobSendOTPView.as_view()),
    path('login_otp_verify',LoginOTPVerifyView.as_view()),
    path('user',UserView.as_view()),
    path('logout',LogoutView.as_view()),
]
