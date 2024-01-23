from rest_framework import serializers
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from .models import CustomUser
from .utills import Util

class UserSignUpSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','password','password2','profilepic','role']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if(password!=password2):
            raise serializers.ValidationError("password and confirm password deosn't match")
        return data
    
    def create(self,validated_data):
        return CustomUser.objects.create_user(**validated_data) 
    
class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    class Meta:
        model = CustomUser
        fields = ['username','password']

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','profilepic','role']

class UserChangePasswordSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['password','password2']

    def validate(self,data):
        password = data.get('password')
        password2 = data.get('password2')
        user = self.context.get('user')
        if password!=password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return data
    
class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['email']

    def validate(self, data):
        email = data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            link = 'http://127.0.0.1:8000/api/user/reset/password/'+uid+'/'+token+'/'
            body = 'Click Following Link to Reset Your Paaword '+link
            email_data = {
                'subject':'Reset Your Password',
                'body': body,
                'to':email
            }
            Util.send_mail(email_data)
            return data
        else:
            raise serializers.ValidationError("You aren't a registered user")
        
class SendPasswordResetSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['password','password2']

    def validate(self,data):
        try:
            password = data.get('password')
            password2 = data.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password!=password2:
                raise serializers.ValidationError("Password and Confirm Password doesn't match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = CustomUser.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise serializers.ValidationError("Token is not valid or expired")
            user.set_password(password)
            user.save()
            return data
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)
            raise serializers.ValidationError("Token is not valid or expired")