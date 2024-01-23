from django.urls import path

from teacher.views import TeacherDashboard

urlpatterns = [
    path('dashboard/',TeacherDashboard.as_view(),name='teacherDashboard')
]