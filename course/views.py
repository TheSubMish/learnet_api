from typing import Any
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.views.generic.edit import UpdateView

from userlog.renderers import UserRenderers
from teacher.models import Teacher
from teacher.permissions import TeacherPermission
from course.serializers import CourseSerializers,ChapterSerializers
from course.models import Course,Chapter

class CreateCourseView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [TeacherPermission]

    def post(self,request,format=None):
        serializer = CourseSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Course Uploaded successfully'},status=status.HTTP_201_CREATED)
    
class UpdateCourseView(APIView,UpdateView):
    renderer_classes = [UserRenderers]
    permission_classes = [TeacherPermission]
    serializer_class = CourseSerializers

    def get(self,request,slug,format=None):
        course = get_object_or_404(Course,slug=slug)
        serializer = self.serializer_class(course)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,slug,format=None):
        course = get_object_or_404(Course,slug=slug)
        serializer = self.serializer_class(course,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Data Updated Successfully'},status=status.HTTP_200_OK)
    
class CreateChapterView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [TeacherPermission]
    serialzer_class = ChapterSerializers
    
    def post(self,request,slug,format=None):
        serializer = self.serialzer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Chapter Uploaded successfully'},status=status.HTTP_201_CREATED)