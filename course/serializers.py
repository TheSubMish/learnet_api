from rest_framework import serializers

from course.models import Course,Chapter,Test

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
    
class ChapterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id','course','chapterName','chapterBody']

    def validate(self,data):
        courseId = data.get('course').pk
        course = Course.objects.get(id=courseId)
        chapterName = data.get('chapterName')
        chapter = chapterName.lower()
        if self.instance is None:
            if Chapter.objects.filter(course=course,chapterName=chapter).exists():
                raise serializers.ValidationError("Chapter with name already exists")
        return data
    
    def create(self, validated_data):
        return Chapter.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.chapterName = validated_data.get('chapterName',instance.chapterName)
        instance.chapterBody = validated_data.get('chapterBody',instance.chapterBody)
        instance.save()
        return instance
    
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id','course','title','question','option1','option2','option3','option4','corAns']

    def create(self, validated_data):
        return Test.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.question = validated_data.get('question',instance.question)
        instance.option1 = validated_data.get('option1',instance.option1)
        instance.option2 = validated_data.get('option2',instance.option2)
        instance.option3 = validated_data.get('option3',instance.option3)
        instance.option4 = validated_data.get('option4',instance.option4)
        instance.corAns = validated_data.get('corAns',instance.corAns)
        instance.save()
        return instance