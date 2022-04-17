from django.contrib import admin
from django.urls import path,include

from grades.views import GradesView, VediosView
urlpatterns = [
    path('usergrades',GradesView.as_view()),
    path('gradeVideos',VediosView.as_view()),
    
]
