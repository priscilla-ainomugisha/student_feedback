from django.urls import path
from . import views

urlpatterns = [
    # path("", views.signin, name = "signin"),
    path("", views.index, name="index"),
    path("base/", views.base, name="base"),
    path("home/", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
]
