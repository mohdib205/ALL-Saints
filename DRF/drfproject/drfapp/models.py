from django.db import models

# Create your models he

class Products(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    price=models.IntegerField()
    stock=models.IntegerField()

# Employee-- name,id,salary,designation

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    product=models.ForeignKey(Products, on_delete=models.CASCADE) #One to Many 
    quantity= models.IntegerField()

class Carousal(models.Model):
    id=models.AutoField(primary_key=True)
    image=models.ImageField(upload_to="carousal/")
    files=models.FileField()

    