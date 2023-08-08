from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("course/", views.course),
    path("facilities/", views.facilities),
    path("instructors/", views.instructor),
    path("signin/", views.signin),
    path("logout/", views.signout),
]
