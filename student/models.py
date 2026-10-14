from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=255)

    age = models.IntegerField()

    roll_no = models.IntegerField(unique=True)

    gender = models.CharField(max_length=1,choices=[('M','Male'),('F','Female'),('O','Other')])

    email = models.EmailField()

    department = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

