from django.urls import path
from .views import ApiStudentsAll,ApiStudent,ApiStudentPosition
urlpatterns = [
    path('students/',ApiStudentsAll.as_view(),name = 'studentsList'),
    path('students/<search>',ApiStudent.as_view(), name = 'student'),
    path('positions/',ApiStudentPosition.as_view(),name = 'studentsList')
]