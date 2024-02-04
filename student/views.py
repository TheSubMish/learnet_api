from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from userlog.renderers import UserRenderers
from student.permissions import StudentPermission

class StudentDashboard(APIView):
    permission_classes = [StudentPermission]
    renderer_classes = [UserRenderers]

    def get(self,request,format=None):
        teacher = get_object_or_404(Teacher, user=request.user)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,format=None):
        teacher = get_object_or_404(Teacher, user=request.user)
        serializer = TeacherSerializer(teacher,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Data Updated Successfullly'}, status=status.HTTP_200_OK)