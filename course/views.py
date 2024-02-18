from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from userlog.renderers import UserRenderers
from teacher.permissions import TeacherPermission
from course.serializers import CourseSerializer,ChapterSerializers,TestSerializers
from course.models import Course,Chapter,Test

class CreateCourseView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated,TeacherPermission]

    def post(self,request,format=None):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Course Uploaded successfully'},status=status.HTTP_201_CREATED)
    
class UpdateCourseView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated,TeacherPermission]
    serializer_class = CourseSerializer

    def get(self,request,slug,format=None):
        course = get_object_or_404(Course,slug=slug)
        serializer = self.serializer_class(course)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,slug,format=None):
        course = get_object_or_404(Course,slug=slug)
        serializer = self.serializer_class(course,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Course Updated Successfully'},status=status.HTTP_200_OK)
    
class DeleteCourseView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated,TeacherPermission]
    serializer_class = CourseSerializer

    def delete(self,request,slug,format=None):
        course = get_object_or_404(Course,slug=slug)
        course.delete()
        return Response({'msg':'Course Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)
    
class CreateChapterView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated,TeacherPermission]
    serializer_class = ChapterSerializers
    
    def post(self,request,slug,format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Chapter Uploaded Successfully'},status=status.HTTP_201_CREATED)
    
class UpdateChapterView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated,TeacherPermission]
    serializer_class = ChapterSerializers

    def get(self,request,slug,uid,format=None):
        chapter = get_object_or_404(Chapter,id=uid)
        serializer = self.serializer_class(chapter)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,slug,uid,format=None):
        chapter = get_object_or_404(Chapter,id=uid)
        serializer = self.serializer_class(chapter,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Chapter Updated Successfully'},status=status.HTTP_200_OK)
    
class DeleteChapterView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated,TeacherPermission]
    serializer_class = ChapterSerializers

    def delete(self,request,slug,uid,format=None):
        chapter = get_object_or_404(Chapter,id=uid)
        chapter.delete()
        return Response({'msg':'Chapter Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)
    
class CreateTestView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated,TeacherPermission]
    serializer_class = TestSerializers

    def post(self,request,slug,format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Test Uploaded Successfully'},status=status.HTTP_201_CREATED)
    
class UpdateTestView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated,TeacherPermission]
    serializer_class = TestSerializers

    def get(self,request,slug,uid,format=None):
        test = get_object_or_404(Test,id=uid)
        serializer = self.serializer_class(test)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,slug,uid,format=None):
        test = get_object_or_404(Test,id=uid)
        serializer = self.serializer_class(test,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Test Updated Successfully'},status=status.HTTP_200_OK)
    
class DeleteTestView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated,TeacherPermission]
    serializer_class = TestSerializers

    def delete(self,request,slug,uid,format=None):
        test = get_object_or_404(Test,id=uid)
        test.delete()
        return Response({'msg':'Test Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)