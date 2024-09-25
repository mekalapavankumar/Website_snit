from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.contrib import messages
from SNIT_WebApp import settings
from .models import UserRegistration, JobApplication, User
from .forms import RegistrationForm, JobApplicationForm, LoginForm
from django.urls import reverse_lazy

def navbar(request):
    return render(request, 'websites/navbar.html')

def home(request):
    return render(request, 'websites/home.html')

def testimonials(request):
    return render(request, 'websites/testimonials.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                form.add_error('confirm_password', 'Passwords do not match')
            else:
                form.save()
                return redirect('registration_success')
    else:
        form = RegistrationForm()
    return render(request, 'websites/register.html', {'form': form})

def registration_success(request):
    return render(request, 'websites/registration_success.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_success')
    else:
        form = LoginForm()
    return render(request, 'websites/login.html', {'form': form})

def login_success(request):
    return render(request, 'login_success.html')

def login_success(request):
    return render(request,'websites/login_success.html')

def career(request):
    return render(request, 'websites/career.html')

def organisation_details(request):
    return render(request, 'websites/organisation_details.html')

def about(request):
    return render(request, 'websites/about.html')

def privacy_policies(request):
    return render(request, 'websites/privacy.html')

def terms_conditions(request):
    return render(request, 'websites/terms_conditions.html')

def contactus(request):
    return render(request, 'websites/Contactus.html')

def FAQ(request):
    return render(request,'websites/FAQ.html')

def job_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Validate data before saving
            email_address = form.cleaned_data['email_address']

            # Check if email already exists in the database
            if JobApplication.objects.filter(email_address=email_address).exists():
                form.add_error('email_address', 'Email already exists. Please use a different email.')
            else:
                # Save the form data
                form.save()
                messages.success(request, 'Job application submitted successfully.')
                return render(request, 'websites/job_application.html', {'form': JobApplicationForm()})

            # Check if phone number is valid
            phone = form.cleaned_data['phone_number']
            if not phone.isdigit() or len(phone) != 10:
                messages.error(request, 'Invalid phone number. Please enter a 10-digit phone number.')
                return render(request, 'websites/job_application.html', {'form': form})

            # Check if resume is a valid file
            resume = form.cleaned_data['resume_cv']
            if not resume:
                messages.error(request, 'Please upload a valid resume.')
                return render(request, 'websites/job_application.html', {'form': form})

            # No need to save the form data again
            messages.success(request, 'Job application submitted successfully.')
            return render(request, 'websites/job_application.html', {'form': JobApplicationForm()})
        else:
            messages.error(request, 'Invalid form data. Please check the form and try again.')
    else:
        form = JobApplicationForm()
    return render(request, 'websites/job_application.html', {'form': form})

def job_application_success(request):
    return render(request, 'websites/job_application_success.html')
    

def send_mail_page(request):
    context = {}

    if request.method=='POST':
         name = request.POST.get('name')
         email = request.POST.get('email')  # User's email (the one sending the message)
         message_content = request.POST.get('message')
        
         if name and email and message_content:
            try:
                # Prepare the email content
                subject = f"New Contact Us Message from {name}"
                message = f"Message from: {name}\nEmail: {email}\n\nMessage:\n{message_content}"
                
                # Send the email
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,  # Sender's email (your email in settings.py)
                    [settings.EMAIL_HOST_USER],  # The recipient (your email)
                    fail_silently=False,
                )
                context['result'] = 'Email sent successfully!'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
         else:
            context['result'] = 'All fields are required'
    
    return render(request, "websites/mail_sent.html", context)