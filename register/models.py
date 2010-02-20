from django.db import models

class Student_details(models.Model):
    name = models.CharField(max_length=100)
    regno = models.CharField(max_length=20,primary_key=True)
    coll = models.CharField(max_length=100,default="Manipal Institute of Technology")
    semester = models.IntegerField()
