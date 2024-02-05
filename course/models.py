from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.db import models

from teacher.models import Teacher

# Create your models here.
cousreCategory = (
    (0,'--------'),
    ('1','HTML'),
    ('2','CSS'),
    ('3','JavaScript'),
    ('4','Python'),
    ('5','Data Analysis'),
    ('6','Data Structure and Algorithms'),
    ('7','Natural Language Processing'),
    ('8','Machine Learning')
)

class Course(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    courseTitle = models.CharField(max_length=100,null=False)
    slug = models.SlugField(max_length=100,null=True)
    courseDescrip = RichTextField()
    category = models.CharField(max_length=30,choices=cousreCategory)
    courseImage = models.ImageField(upload_to='courseImage',null=False)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.courseTitle = self.courseTitle.lower()
        self.slug = slugify(self.courseTitle)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.courseTitle
    
class Chapter(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    chapterName = models.CharField(max_length=100)
    chapterBody = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        self.chapterName = self.chapterName.lower()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.chapterName
    
class Test(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100,null=True)
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    corAns = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question