from imaplib import _Authenticator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .forms import CampusFacilitiesFeedbackForm, SignInForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import CourseInfo
from .models import YearOfStudy
from .models import Semester
from .models import Card_info
import re
from .forms import MultiStepForm,Card_info
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage



# Create your views here
# Create your views here.
def index(request):
    selected_semester = request.GET.get("semester", "1")  # Default to "1" if not provided
    selected_year = int(request.GET.get("year_of_study", 1))  # Default to 1 if not provided


    # Query the database for course units based on the selected semester and year
    course_units = CourseInfo.objects.filter(semester=selected_semester, year_of_study=selected_year)
    course_units_list = [CourseInfo.course_name for CourseInfo in course_units]


    course = CourseInfo.objects.all()
    semester_data = set([x.semester for x in course])
    
    years_of_study = set([x.year_of_study for x in course])
    return render(request, 'index.html', {'semester_data': semester_data, 'years_of_study': years_of_study, 'courses': course_units_list})



def signin(request):
    return render(request, "signin.html")

def base(request):
    return render(request, "base.html")



def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            print('No User')
            return HttpResponseRedirect("/login")
        else:
            print('User')
            return HttpResponseRedirect("/index")
    else:
        return render(request, "login.html")


def logout(request):
    return render(request, "logout.html")

def form(request):
    return render(request, "form.html")

def facilitiesform(request):
    return render(request, "facilitiesform.html")


@login_required()
def profile(request):
    return render(request, 'feedback/profile.html')

def register(request):
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
    return render(request, "instructor_feedback.html")


@login_required(login_url="/login")
def course_feedback(request):
    return render(request, "course_feedback.html")


@login_required(login_url="/login")
def index(request):
    return render(request, "index.html")
def home(request):
    return render(request, 'feedback/home.html')

def get_course_units(request):
    if request.method == "GET":
        selected_semester = request.GET.get("semester", "1")  # Default to "1" if not provided
        selected_year = int(request.GET.get("year_of_study", 1))  # Default to 1 if not provided


        # Query the database for course units based on the selected semester and year
        course_units = CourseInfo.objects.filter(semester=selected_semester, year_of_study=selected_year)
        course_units_list = [CourseInfo.COURSE_NAME for CourseInfo in course_units]

        return JsonResponse({"course_units": course_units_list})

    return JsonResponse({"error": "Invalid request method."}, status=400)


def success_page_view(request):
    return render(request, 'success_page.html')


def multi_step_form_view(request):
    if request.method == 'POST':
        form = MultiStepForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Form submitted successfully!')
            return redirect('index') 
            
    else:
        form = MultiStepForm()

    return render(request, 'form.html', {'form': form})

def facilities(request):
    if request.method == 'POST':
        form = CampusFacilitiesFeedbackForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Form submitted successfully!')
            return redirect('index') 
            
    else:
        form = CampusFacilitiesFeedbackForm()

    return render(request, 'facilitiesform.html', {'form': form})



def show_message_form_condition(wizard):
    # try to get the cleaned data of step 1
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    # check if the field ``leave_message`` was checked.
    return cleaned_data.get('leave_message', True)

class ContactWizard(SessionWizardView):

    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

from .forms import SignInForm

def sign_in_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            # Process sign-in logic (e.g., authentication, session handling, etc.)
            # Redirect to another page after successful sign-in.
            return redirect('index')
    else:
        form = SignInForm()

    return render(request, 'login.html', {'form': form})
