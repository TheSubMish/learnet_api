from rest_framework import serializers
import re

from .models import Teacher
from userlog.serializers import UserProfileSerializer

class TeacherSerializer(serializers.ModelSerializer):
    # user = UserProfileSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self,validated_data):
        return Teacher.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.city = validated_data.get('city', instance.city)
        instance.district = validated_data.get('district', instance.district)
        instance.edubackground = validated_data.get('edubackground', instance.edubackground)
        instance.teachexp = validated_data.get('teachexp', instance.teachexp)
        instance.save()
        return instance
    