from django.db import models

# Create your models here.
class database(models.Model):
    title=models.CharField(max_length=225)
    description=models.TextField(max_length=255)
    name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class Contact(models.Model):
    name=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
