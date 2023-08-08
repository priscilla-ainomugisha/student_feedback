from django.http import HttpResponseRedirect
from django.shortcuts import render

# from django.contrib.auth.models import User, authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    return render(request, "admin_index.html")


@login_required(login_url="/administrator/signin")
def course(request):
    return render(request, "admin_index.html", context={"pages": "course", "value": True})


@login_required(login_url="/administrator/signin")
def instructor(request):
    return render(request, "admin_index.html", context={"pages": "instructors"})


@login_required(login_url="/administrator/signin")
def facilities(request):
    return render(request, "admin_index.html", context={"pages": "facilities"})


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
                return HttpResponseRedirect("/login")
    else:
        return render(request, "sign_in.html")


def signout(request):
    logout(request=request)
    return render(request, "sign_in.html")
