from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from .models import Customer, Response, Questionnaire, UserProfile

@staff_member_required  # This decorator ensures only staff (Admin) users can access these views
def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'admin_pages/list_customers.html', {'customers': customers})
    

def customer_responses(request, customer_id):
    # Assuming you have retrieved customer and their responses from the database
    customer = Customer.objects.get(id=customer_id)
    responses = Response.objects.filter(customer=customer)  # Assuming Response is a model representing customer responses

    return render(request, 'admin_pages/customer_responses.html', {'customer': customer, 'customer_responses': responses})

@staff_member_required
def create_questionnaire(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        
        # Create a new Questionnaire object
        new_questionnaire = Questionnaire.objects.create(
            question=question,
            option1=option1,
            option2=option2,
            option3=option3
        )
        messages.success("You've successfully created a questionnaire!")
        return redirect('create_questionnaire.html')  # Replace 'success_page' with your URL name
    
    return render(request, 'admin_pages/create_questionnaire.html')


# Create your views here.
def index(request):
    return render(request, 'registration/index.html')  # Render a different template for the root URL

def customer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)  # Replace with your form instance
        if form.is_valid():
            # Handle form submission logic
            # For instance, authenticate user, perform login, etc.
            return HttpResponse("Success")  # Replace with your desired response
        
        # If form is not valid, handle accordingly (e.g., show errors)
        return render(request, 'questionnaire/admin_questionnaires.html')
    
    else:
        form = AuthenticationForm()  # Replace with your form instance
        return render(request, 'login/customer_login.html', {'form': form})


def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)  # Replace with your form instance
        if form.is_valid():
            # Handle form submission logic
            # For instance, authenticate user, perform login, etc.
            return HttpResponse("Success")  # Replace with your desired response
        
        # If form is not valid, handle accordingly (e.g., show errors)
        return render(request, 'admin_pages/admin_dashboard.html')
    
    else:
        form = AuthenticationForm()  # Replace with your form instance
        return render(request, 'login/admin_login.html', {'form': form})


# User registration
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_type = request.POST.get('user_type')
            user = form.save()

            # Check if user_type is provided
            if user_type:
                # Create UserProfile instance with user_type
                profile = UserProfile.objects.create(user=user, user_type=user_type)
                # Handle success messages and redirection here
                messages.success(request, 'Registration successful. Please log in.')

                # Redirect to the appropriate login page
                if user_type == 'admin':
                    return redirect('admin_login')                
                else:
                    return redirect('customer_login')
            else:
                # Handle errors related to user_type not being provided
                messages.error(request, 'User type is required.')

                # Redirect back to the registration page if there's an error
                return redirect('register')  # Replace 'register' with your register URL name
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


def admin_questionnaires(request):
    # Assuming the Questionnaire model has a field 'created_by' referencing the admin
    admin_questionnaires = Questionnaire.objects.filter(creator=request.user)
    return render(request, 'admin_questionnaires.html', {'admin_questionnaires': admin_questionnaires})
