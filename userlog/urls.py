from django.urls import path
from .views import UserSignUpView,UserLoginView,UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView

urlpatterns = [
    path('signup/',UserSignUpView.as_view(),name='signup'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('change/password/',UserChangePasswordView.as_view(),name='changePassword'),
    path('reset/password/',SendPasswordResetEmailView.as_view(),name='reset-mail-send'),
    path('reset/password/<uid>/<token>/',UserPasswordResetView.as_view(),name='reset-apssword')
]