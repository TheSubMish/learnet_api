from django.urls import path

from course.views import CreateCourseView,UpdateCourseView,CreateChapterView,UpdateChapterView,CreateTestView,UpdateTestView

urlpatterns = [
    path('addcourse/',CreateCourseView.as_view(),name="create_course"),
    path('update/<slug:slug>/',UpdateCourseView.as_view(),name="update_course"),
    path('addchapter/<slug:slug>/',CreateChapterView.as_view(),name="create_course"),
    path("update/<slug:slug>/chapter/<uid>/",UpdateChapterView.as_view(),name="update_chapter"),
    path("addtest/<slug:slug>/",CreateTestView.as_view(),name="create_test"),
    path("update/<slug:slug>/test/<uid>/",UpdateTestView.as_view(),name="update_test")
]
