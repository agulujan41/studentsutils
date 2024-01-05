from django.contrib import admin
from .models import Alumno as Student
class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student,StudentAdmin)