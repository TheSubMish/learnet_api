from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from userlog.renderers import UserRenderers
from teacher.serializers import TeacherSerializer
from teacher.models import Teacher

class TeacherDashboard(APIView):
    renderer_classes = [UserRenderers]

    def get_object(self,user):
        try:
            return Teacher.objects.get(user=self.request.user)
        except Teacher.DoesNotExist:
            return None
    
    def get(self,request,format=None):
        teacher = self.get_object(request.user)
        if teacher is None:
            return Response({'msg':'Teacher not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,format=None):
        teacher = self.get_object(request.user)
        if teacher is None:
            return Response({'msg':'Teacher not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = TeacherSerializer(teacher,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Data Updated Successfullly'}, status=status.HTTP_201_CREATED)