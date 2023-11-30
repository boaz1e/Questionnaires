from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from .models import Questionnaire


# Create your views here.

# def say_hello(request):
#     return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')  # Render a different template for the root URL

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            # Redirect to a specific page after login (e.g., dashboard)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# User registration
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('login')  # Replace 'login' with your login URL name
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# Questionnaire creation
def create_questionnaire(request):
    if request.method == 'POST':
        # Handle form submission to create a questionnaire
        # Retrieve form data and save it to the Questionnaire model
        # Example:
        title = request.POST['title']
        description = request.POST['description']
        questionnaire = Questionnaire.objects.create(title=title, description=description)
        questionnaire.save()
        pass
    return render(request, 'questionnaire/create_questionnaire.html')



