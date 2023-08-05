from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "admin_index.html")


def course(request):
    return render(request, "admin_index.html", context={"pages": "course"})


def instructor(request):
    return render(request, "admin_index.html", context={"pages": "instructors"})


def facilities(request):
    return render(request, "admin_index.html", context={"pages": "facilities"})
