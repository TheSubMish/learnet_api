from django.shortcuts import get_object_or_404
from course.serializers import CourseSerializers
from teacher.models import Teacher

def save_serailizer(request):
    teacher = get_object_or_404(Teacher, user=request.user)
    currentdata = request.data
    currentdata['teacher'] = teacher.pk
    serializer = CourseSerializers(data=currentdata)
    serializer.is_valid(raise_exception=True)
    serializer.save()