from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render


# Create your views here
def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponseRedirect("/administrator/signin")
        else:
            if user.is_superuser:
                login(request, user)
                return HttpResponseRedirect("/administrator/course")
            else:
                return HttpResponseRedirect("/")
    else:
        return render(request, "auth/signin.html")


def log_out(request):
    logout(request=request)
    return HttpResponseRedirect("/login")


@login_required(login_url="/login")
def facility_feedback(request):
    return render(request, "facility_feedback.html")


@login_required(login_url="/login")
def instructor_feedback(request):
    return render(request, "facility_feedback.html")


@login_required(login_url="/login")
def course_feedback(request):
    return render(request, "facility_feedback.html")


@login_required(login_url="/login")
def index(request):
    if request.user.is_authenticated:
        print(True)
    else:
        print(False)
    return render(request, "index.html")
