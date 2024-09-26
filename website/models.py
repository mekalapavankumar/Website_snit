from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.core import validators
import re

def validate_name(value):
    if not re.match("^[A-Za-z]*$", value):
        raise ValidationError('This field accepts only characters.')

def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Password must be at least 8 characters long.')

#REGISTRATION PAGE CREDENTIALS
class UserRegistration(models.Model):
    first_name = models.CharField(max_length=50, validators=[validate_name])
    last_name = models.CharField(max_length=50, validators=[validate_name])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[validate_password])
    confirm_password = models.CharField(max_length=128, validators=[validate_password])

class Address(models.Model):
    street_address = models.CharField(max_length=255)
    street_address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_zip_code = models.CharField(max_length=20)


#JOB APPLICATION PAGE CREDENTIALS
class JobApplication(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=20)
    position_applied_for = models.CharField(max_length=255)
    resume_cv = models.FileField(upload_to='resumes/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    cover_letter = models.TextField()
    current_level_of_experience = models.CharField(max_length=20, choices=[
        ('Entry Level', 'Entry Level'),
        ('Mid Level', 'Mid Level'),
        ('Senior Level', 'Senior Level'),
        ('Other', 'Other'),
    ])
    earliest_possible_start_date = models.DateField(null=True)
    consent_to_privacy_policy = models.BooleanField(null=True)


#LOGIN PAGE CREDENTIALS
class User(models.Model):
    username = models.CharField(max_length=255, unique=True, validators=[
        validators.RegexValidator(
            re.compile('^[a-zA-Z]+$'), 
            'Enter a valid username', 
            'invalid'
        )
    ])
    password = models.CharField(max_length=255, validators=[
        validators.RegexValidator(
            re.compile('^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+=-{};:"<>,./?]).{8,}$'), 
            'Password should be at least 8 characters, and contain at least one letter, one number, and one special character', 
            'invalid'
        )
    ])

    def set_password(self, password):
        self.password = make_password(password)

    def __str__(self):
        return self.username