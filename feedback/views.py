from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import re
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
    selected_semester = request.GET.get(
        "semester", "1"
    )  # Default to "1" if not provided
    selected_year = int(
        request.GET.get("year_of_study", 1)
    )  # Default to 1 if not provided

    # Query the database for course units based on the selected semester and year
    course_units = CourseInfo.objects.filter(
        semester=selected_semester, year_of_study=selected_year
    )
    course_units_list = [CourseInfo.course_name for CourseInfo in course_units]

    course = CourseInfo.objects.all()
    semester_data = set([x.semester for x in course])

    years_of_study = set([x.year_of_study for x in course])
    return render(
        request,
        "index.html",
        {
            "semester_data": semester_data,
            "years_of_study": years_of_study,
            "courses": course_units_list,
        },
    )


def signin(request):
    return render(request, "signin.html")


def login(request):
    return render(request, "login.html")


def logout(request):
    return render(request, "logout.html")


def facility_feedback(request):
    return render(request, "facility_feedback.html")
