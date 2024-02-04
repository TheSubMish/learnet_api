from rest_framework import serializers

from .models import Teacher
from userlog.serializers import UserProfileSerializer
from course.serializers import CourseSerializer
from course.models import Course

class TeacherSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(required=False)
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = '__all__'
    
    def to_representation(self, instance):
        # Fetch related courses for the teacher instance
        courses = Course.objects.filter(teacher=instance)
        course_serializer = CourseSerializer(courses, many=True)
        representation = super().to_representation(instance)
        representation['courses'] = course_serializer.data
        return representation
    
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.city = validated_data.get('city', instance.city)
        instance.district = validated_data.get('district', instance.district)
        instance.edubackground = validated_data.get('edubackground', instance.edubackground)
        instance.teachexp = validated_data.get('teachexp', instance.teachexp)
        instance.save()
        return instance
     