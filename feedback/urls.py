
from django.urls import path

from . import views

urlpatterns = [
    path("facilities/", views.facility_feedback),
    path("course/", views.course_feedback),
    path("instructors/", views.instructor_feedback),
    path("login/", views.signin, name="login"),
    path("", views.index),
    path("logout/", views.log_out, name="logout"),

    path("", views.home, name='home' ),
    path('index/', views.index, name='index'),
    path('base/', views.base, name='base'),
   
    path('home/register.html', views.register, name='register' ),
    path('login/', views.sign_in_view, name='login' ),
    path('logout/', views.logout, name='logout' ),
    path('profile/', views.profile, name='profile' ),
    path('register/', views.register, name='register' ),
    path('get_course_units/', views.get_course_units, name='get_course_units'),

    path('index/form.html', views. multi_step_form_view, name='form'),
    path('form/', views.multi_step_form_view, name='feedback'),
    path('success-page/', views.success_page_view, name='success-page'),
    path('index/facilitiesform.html/', views.facilities, name='success-page'),
    ]
