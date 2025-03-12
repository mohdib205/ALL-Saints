from django.db import models

# Create your models here.

class Student(models.Model):
    
    name=models.CharField(max_length=20 , primary_key=True)
    age=models.IntegerField(default=18)
    branch=models.CharField(max_length=20 , null=True)
    
    

    
    
    
    
    
    