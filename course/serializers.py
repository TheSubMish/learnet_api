from rest_framework import serializers

from course.models import Course

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','courseTitle','courseDescrip','category','courseImage','slug','teacher']

    def validate(self, data):
        course = data.get('courseTitle')
        course_title = course.lower()
        if self.instance is None:
            if Course.objects.filter(courseTitle=course_title).exists():
                raise serializers.ValidationError("Course with this name already exists")
        else:
            if Course.objects.exclude(pk=self.instance.pk).filter(courseTitle=course_title).exists():
                raise serializers.ValidationError("Course with this name already exists")
        return data


    def create(self, validated_data):
        return Course.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.courseTitle = validated_data.get('courseTitle',instance.courseTitle)
        instance.courseDescrip = validated_data.get('courseDescrip',instance.courseDescrip)
        instance.category = validated_data.get('category',instance.category)
        instance.courseImage = validated_data.get('courseImage',instance.courseImage)
        instance.save()
        return instance