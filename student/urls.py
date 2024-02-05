from django.urls import path

from student.views import StudentDashboardView,ManyCourseView,SingleCourseView,EnrollView,ReadChapterTestView,GiveTestView

urlpatterns = [
    path('dashboard/',StudentDashboardView.as_view(),name="Student_dashboard"),
    path('many-course/',ManyCourseView.as_view(),name="many_course"),
    path('single-course/<slug:slug>/',SingleCourseView.as_view(),name="single_course"),
    path('course-enroll/<slug:slug>/',EnrollView.as_view(),name="course_enroll"),
    path('read/<slug:slug>/',ReadChapterTestView.as_view(),name="read_chapter_test"),
    path('give/<slug:slug>/test/<slug:test_slug>/',GiveTestView.as_view(),name="Give_test")
]
