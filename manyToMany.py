from django.db import models

class Campus(model.Model):
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    
class Student(model.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    campus = models.ManyToManyField(Campus)
    
class Primary_Campus(models.Model):
    campus = models.ForeignKey(Campus)
    student = models.ForeignKey(Student)
    primary = models.BooleanField()
