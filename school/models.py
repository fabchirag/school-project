from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

class Student(models.Model):
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    age = models.IntegerField()
    email = models.EmailField()


