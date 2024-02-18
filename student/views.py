from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from userlog.renderers import UserRenderers
from student.permissions import StudentPermission
from student.serializers import StudentDashboardSerializer,StudentCourseSerializer,EnrollSerializer,ReadChapterTestSerializer,StudentMarkSerializer
from student.models import Student,Enroll
from course.models import Course,Chapter,Test

class StudentDashboardView(APIView):
    permission_classes = [IsAuthenticated,StudentPermission]
    renderer_classes = [UserRenderers]
    serializer_class = StudentDashboardSerializer

    def get(self,request,format=None):
        student = get_object_or_404(Student, user=request.user)
        serializer = self.serializer_class(student)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,format=None):
        student = get_object_or_404(Student, user=request.user)
        serializer = self.serializer_class(student,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Student Data Updated Successfullly'}, status=status.HTTP_200_OK)
    
class ManyCourseView(ListAPIView):
    renderer_classes = [UserRenderers]
    pagination_class = PageNumberPagination
    queryset = Course.objects.all()
    serializer_class = StudentCourseSerializer

class SingleCourseView(APIView):
    renderer_classes = [UserRenderers]
    serializer_class = StudentCourseSerializer

    def get(self,request,slug,format=None):
        course = get_object_or_404(Course,slug=slug)
        serializer = self.serializer_class(course)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class EnrollView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated,StudentPermission]
    serializer_class = EnrollSerializer

    def get(self,request,slug,format=None):
        course = get_object_or_404(Course,slug=slug)
        student = get_object_or_404(Student,user=request.user)
        enrollment, created = Enroll.objects.get_or_create(student=student, course=course)
        serializer = self.serializer_class(enrollment)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class ReadChapterTestView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated,StudentPermission]
    serializer_class = ReadChapterTestSerializer

    def get(self,request,slug,format=None):
        course = get_object_or_404(Course,slug=slug)
        serializer = self.serializer_class(course)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class GiveTestView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated,StudentPermission]
    serializer_class = StudentMarkSerializer

    def post(self,request,slug,test_slug,format=None):
        score = 0
        user_answers = request.data
        tests = list(Test.objects.filter(slug=test_slug))
        for test in tests:
            if test.corAns in user_answers.values():
                score=score+1
        student = Student.objects.get(user=request.user)
        print(tests[:1])
        data = {
            'student':student.pk,
            'test':test.pk,
            'score':score
        }
        serializer = self.serializer_class(data=data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Student Data Updated Successfullly'}, status=status.HTTP_200_OK)