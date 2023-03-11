from django.db import models

# Create your models here.

class Student(models.Model):
    StusdentId = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=300)
    StudentLastName = models.CharField(max_length=300)
    StudentAccount = models.DateField()
    