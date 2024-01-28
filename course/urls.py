from django.urls import path

from course.views import CreateCourseView,UpdateCourseView

urlpatterns = [
    path('addcourse/',CreateCourseView.as_view(),name="create_course"),
    path('update/<slug:slug>/',UpdateCourseView.as_view(),name="update_course")
]
