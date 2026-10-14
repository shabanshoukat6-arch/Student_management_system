from django import forms
from student.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = ['name','age','roll_no','gender','email','department']

        