from django import forms
from .models import UserRegistration, Address, JobApplication, User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ('first_name', 'last_name', 'email', 'password', 'confirm_password')
        widgets = {
            'password': forms.PasswordInput(attrs={'required': 'required'}),
            'confirm_password': forms.PasswordInput(attrs={'required': 'required'}),
        }

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            confirm_password = cleaned_data.get('confirm_password')
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match")
            return cleaned_data

        def save(self, commit=True):
            user = super().save(commit=False)
            user.username = f"{self.cleaned_data['username']}_{self.cleaned_data['lastname']}"
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ('first_name', 'last_name', 'email_address', 'phone_number', 'position_applied_for', 'resume_cv', 'cover_letter', 'current_level_of_experience', 'earliest_possible_start_date')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    )
    