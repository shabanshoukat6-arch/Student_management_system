
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from student.forms import StudentForm
from student.models import Student


def home(request):
    form = StudentForm()
    return render(request, 'student/home.html', {'form': form})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Student added successfully!"
            )
            return redirect('student_list')

        messages.error(request, "Please correct the errors below.")

    else:
        form = StudentForm()

    return render(request, 'student/home.html', {'form': form})


def student_list(request):
    students = Student.objects.all().order_by('id')

    return render(
        request,
        'student/student_list.html',
        {'students': students}
    )


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Student updated successfully!"
            )
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'student/edit_student.html',
        {
            'form': form,
            'student': student
        }
    )


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        messages.success(
            request,
            "Student deleted successfully!"
        )
        return redirect('student_list')

    return render(
        request,
        'student/delete_student.html',
        {'student': student}
    )
