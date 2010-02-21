from django.db import models

## models for taking student details from a CSV file ( absolute path of file in views.py )
class Student_details(models.Model):
    name = models.CharField(max_length=100)
    regno = models.CharField(max_length=20,primary_key=True)
    coll = models.CharField(max_length=100,default="Manipal Institute of Technology")
    semester = models.IntegerField()

# model for storing a successful registration
class RegisteredStudent(models.Model):
    name = models.CharField(max_length=100)
    regno = models.CharField(max_length=20)
    coll = models.CharField(max_length=100)
    

