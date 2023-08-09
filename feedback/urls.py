from django.urls import path
from . import views

urlpatterns = [
    path("facilities/", views.facility_feedback),
    path("course/", views.course_feedback),
    path("instructors/", views.instructor_feedback),
    path("login/", views.signin, name="login"),
    path("", views.index),
    path("logout/", views.log_out, name="logout"),
]
