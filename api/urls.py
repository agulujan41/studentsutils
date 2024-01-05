from django.urls import path
from .views import ApiStudentsAll,ApiStudent
urlpatterns = [
    path('students/',ApiStudentsAll.as_view(),name = 'studentsList'),
    path('students/<search>',ApiStudent.as_view(), name = 'student')
]