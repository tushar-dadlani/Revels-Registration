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
    regtime = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.regno

	
#class Event(models.Model):
#    student_id =  models.ForeignKey('RegisteredStudent') 
    	
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name 	    

class Event(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey('Category')
    participants = models.IntegerField()
    def __unicode__(self):
        return self.name	    
    
class Team(models.Model):
    event = models.ForeignKey('Event') 
    def __unicode__(self):
        return str(self.id)	    
