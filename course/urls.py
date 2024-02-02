from django.urls import path

from course.views import CreateCourseView,UpdateCourseView,DeleteCourseView,CreateChapterView,UpdateChapterView,DeleteChapterView,CreateTestView,UpdateTestView,DeleteTestView

urlpatterns = [
    path('addcourse/',CreateCourseView.as_view(),name="create_course"),
    path('update/<slug:slug>/',UpdateCourseView.as_view(),name="update_course"),
    path('delete/<slug:slug>/',DeleteCourseView.as_view(),name="delete_course"),
    path('addchapter/<slug:slug>/',CreateChapterView.as_view(),name="create_course"),
    path("update/<slug:slug>/chapter/<uid>/",UpdateChapterView.as_view(),name="update_chapter"),
    path("delete/<slug:slug>/chapter/<uid>/",DeleteChapterView.as_view(),name="delete_chapter"),
    path("addtest/<slug:slug>/",CreateTestView.as_view(),name="create_test"),
    path("update/<slug:slug>/test/<uid>/",UpdateTestView.as_view(),name="update_test"),
    path("delete/<slug:slug>/test/<uid>/",DeleteTestView.as_view(),name="delete_test")
]
