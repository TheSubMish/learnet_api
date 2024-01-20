from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from userlog.serializers import UserSignUpSerializer,UserLoginSerializer,UserProfileSerializer,UserChangePasswordSerializer,SendPasswordResetEmailSerializer,SendPasswordResetSerializer
from userlog.renderers import UserRenderers

# generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserSignUpView(APIView):
    renderer_classes = [UserRenderers]

    def post(self,request,format=None):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        login(request,user)
        return Response({'token':token,'msg':'SignUp Successful'}, status=status.HTTP_201_CREATED)
    
class UserLoginView(APIView):
    renderer_classes = [UserRenderers]

    def post(self,request,format=None):

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            login(request,user)
            return Response({'token':token,'msg':'LogIn Successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors':{'non_field_errors':['Username or Password is not valid']}},status=status.HTTP_404_NOT_FOUND)
        
    
class UserProfileView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
        serializer = UserChangePasswordSerializer(data=request.data,context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password changed successfully'}, status=status.HTTP_200_OK)
    
class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderers]
    def post(self,request,format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password reset mail sent. Check Your Mail'}, status=status.HTTP_200_OK)
    
class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderers]
    def post(self,request,uid,token,format=None):
        serializer = SendPasswordResetSerializer(data=request.data,context={'uid':uid,'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password reset successfully'}, status=status.HTTP_200_OK)