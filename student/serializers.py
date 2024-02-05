from rest_framework import serializers

from userlog.serializers import UserProfileSerializer
from course.serializers import CourseSerializer,ChapterSerializers,TestSerializers
from course.models import Course,Chapter,Test
from student.models import Student,Enroll,StudentMark

class EnrollSerializer(serializers.ModelSerializer):
    course = CourseSerializer(required=False)

    class Meta:
        model = Enroll
        fields = '__all__'

class StudentDashboardSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(required=False)
    enrolls = EnrollSerializer(many=True,read_only=True)

    class Meta:
        model = Student
        fields = '__all__'

    def to_representation(self, instance):
        enrolls = Enroll.objects.filter(student=instance)
        enroll_serializer = EnrollSerializer(enrolls, many=True)
        representation = super().to_representation(instance)
        representation['enrolls'] = enroll_serializer.data
        return representation
    
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.city = validated_data.get('city', instance.city)
        instance.district = validated_data.get('district', instance.district)
        instance.edubackground = validated_data.get('edubackground', instance.edubackground)
        instance.save()
        return instance
    
class StudentCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id','courseTitle','courseDescrip']
    
class ReadChapterTestSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializers(many=True, read_only=True)
    tests = TestSerializers(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id','courseTitle','chapters','tests']

    def to_representation(self, instance):
        chapters = Chapter.objects.filter(course=instance)
        chapter_serializer = ChapterSerializers(chapters,many=True)
        tests = Test.objects.filter(course=instance)
        test_serializer = TestSerializers(tests,many=True)
        representation = super().to_representation(instance)
        representation['chapters'] = chapter_serializer.data
        representation['tests'] = test_serializer.data
        return representation

    
class StudentMarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentMark
        fields = ['id','student','test','score']

    def create(self, validated_data):
        student = validated_data.pop('student')
        test = validated_data.pop('test')
        score = validated_data.pop('score')

        instance, created = StudentMark.objects.update_or_create(
            student=student,
            test=test,
            defaults={'score': score}
        )
        return instance
