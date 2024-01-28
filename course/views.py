from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from userlog.renderers import UserRenderers
from teacher.models import Teacher
from teacher.permissions import TeacherPermission
from course.serializers import CourseSerializers
from course.models import Course
from course.utills import save_serailizer
class CreateCourseView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [TeacherPermission]

    def post(self,request,format=None):
        teacher = get_object_or_404(Teacher, user=request.user)
        currentdata = request.data
        currentdata['teacher'] = teacher.pk
        serializer = CourseSerializers(data=currentdata)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Course Uploaded successfully'},status=status.HTTP_201_CREATED)
    
class UpdateCourseView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [TeacherPermission]
    serializer_class = CourseSerializers

    def get(self,request,slug,format=None):
        course = get_object_or_404(Course,slug=slug)
        serializer = self.serializer_class(course)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,slug,format=None):
        teacher = get_object_or_404(Teacher, user=request.user)
        currentdata = request.data
        currentdata['teacher'] = teacher.pk
        course = get_object_or_404(Course,slug=slug)
        serializer = CourseSerializers(course,data=currentdata)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Data Updated Successfully'},status=status.HTTP_200_OK)