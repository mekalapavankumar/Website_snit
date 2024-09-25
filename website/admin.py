from django.contrib import admin
from .models import JobApplication

# Register your models here.

class AdminJobApplication(admin.ModelAdmin):
    list_display= ('first_name', 'last_name', 'email_address', 'phone_number', 'position_applied_for', 'resume_cv', 'cover_letter', 'current_level_of_experience', 'earliest_possible_start_date')


admin.site.register(JobApplication,AdminJobApplication)
 