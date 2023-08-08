from django.urls import path
from . import views

urlpatterns = [
    path("facilities/", views.facility_feedback, name="index"),
    path("course/", views.course_feedback, name="index"),
    path("instructors/", views.instructor_feedback, name="index"),
    path("login/", views.signin, name="login"),
    path("", views.index),
    path("logout/", views.log_out, name="logout"),
]
