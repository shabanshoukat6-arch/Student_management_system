
from django.urls import path
from student.views import (
    home,
    add_student,
    student_list,
    edit_student,
    delete_student,
)

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_student, name='add_student'),
    path('students/', student_list, name='student_list'),
    path('students/edit/<int:pk>/', edit_student, name='edit_student'),
    path('students/delete/<int:pk>/', delete_student, name='delete_student'),
]