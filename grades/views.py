from django.shortcuts import render
from requests import Response

from grades.models import Grade, Video
from grades.serializers import GradeSerializer, VideoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from users.models import Student
# Create your views here.


class GradesView(APIView):
    """
    View to list all grades in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """_summary_
        return a list of all grades
        """
        userid = request.query_params["userId"]
        print(userid)
        student_grades =[]
        try:
            student_grades =Student.objects.get(userCode =userid).grade
        except Exception as e:
            print(e)
        
        # grades = Grade.objects.get( )
        # grades.filter()
        grade_serializer = GradeSerializer(student_grades, many=True)

        return Response(grade_serializer.data)
    
class VediosView(APIView):
    """
    View to list all vedios in the grade.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """_summary_
        return a list of all vedios
        """
        gradeId = request.query_params["grade"]
        print(gradeId)
        video_list =[]
        
        print(video_list)
        try:
            video_list = Video.objects.filter(grade = gradeId)
        except Exception as e:
            print(e)
        video_serializer = VideoSerializer(video_list,many = True)
        
        return Response(video_serializer.data)