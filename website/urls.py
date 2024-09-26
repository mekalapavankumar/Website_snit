from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home, name='home'),
    path('navbar/', views.navbar, name='navbar'),
    path('home/', views.home, name='home'),  
    path('register/', views.register, name='register'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('login/', views.login_view, name='login'),
    path('login_success/', views.login_success, name="login_success"),
    path('career/', views.career, name='career'),
    path('organisation_details/', views.organisation_details, name='organisation_details'),
    path('about/', views.about, name='about'),
    path('privacy_policies/', views.privacy_policies, name='privacy_policies'),
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
    path('contactus/', views.contactus, name="contactus"),
    path('send_email/', views.send_email, name="send_email"),
    path('faq/', views.FAQ, name="faq"),
    path('job_application/', views.job_application, name='job_application'),
    path('job_application_success/', views.job_application_success, name='job_application_success'),
]
