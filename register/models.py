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
    contact = models.CharField(max_length=11)
    email = models.CharField(max_length=50)	
    address = models.CharField(max_length=250)
    team = models.ForeignKey('Team',null=True)

	
#class Event(models.Model):
#    student_id =  models.ForeignKey('RegisteredStudent') 
    	
class Category(models.Model):
    name = models.CharField(max_length=20)
    head = models.CharField(max_length=40)

class Event(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey('Category')
    head = models.CharField(max_length=40)
    participants = models.IntegerField()
    
class Team(models.Model):
    event = models.ForeignKey('Event') 
    
