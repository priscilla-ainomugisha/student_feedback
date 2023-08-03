from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "index.html")


# def signin(request):
#     return render(request, "signin.html")

def base(request):
    return render(request, "base.html")

#def home(request):
    #return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def logout(request):
    return render(request, "logout.html")


@login_required()
def profile(request):
    return render(request, 'feedback/profile.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'feedback/register.html', {'form': form})


def home(request):
    return render(request, 'feedback/home.html')
