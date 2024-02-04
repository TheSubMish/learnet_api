from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from userlog.renderers import UserRenderers
from teacher.serializers import TeacherSerializer
from teacher.models import Teacher
from teacher.permissions import TeacherPermission

class TeacherDashboard(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [TeacherPermission]
    
    def get(self,request,format=None):
        teacher = get_object_or_404(Teacher, user=request.user)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def patch(self,request,format=None):
        teacher = get_object_or_404(Teacher, user=request.user)
        serializer = TeacherSerializer(teacher,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Data Updated Successfullly'}, status=status.HTTP_200_OK)