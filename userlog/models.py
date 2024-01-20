from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import os

def profile_pic_file_path(instance, filename):
    # Generate a unique image name based on the username
    if filename is None:
        raise ValidationError('Upload a file')
    base_filename, file_extension = os.path.splitext(filename)
    ext = file_extension.lower()
    allowed_extensions = ['.png', '.jpg', '.jpeg']
    if ext not in allowed_extensions:
        raise ValidationError('Only .png, .jpg or .jpeg extenstions are allowed.')
    return f'profilepic/{instance.username}{file_extension}'

class CustomUserManager(BaseUserManager):
    def create_user(self, username,email, firstname=None,lastname=None, password=None, password2=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username,email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=100,unique=True)
    profilepic = models.ImageField(default='profilepic\profile.jpg',upload_to=profile_pic_file_path)
    role = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username