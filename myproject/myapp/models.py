from django.db import models

# Create your models here.
class student(models.Model):
    fullname=models.CharField(max_length=100)  #attributes
    email=models.EmailField(max_length=10)
    contact=models.CharField(max_length=50)
    city=models.CharField(max_length=10)

class teacher(models.Model):
    fullname=models.CharField(max_length=100)  #attributes
    email=models.EmailField(max_length=20)
    contact=models.CharField(max_length=50)
    city=models.CharField(max_length=10)


class emp(models.Model):
    fullname=models.CharField(max_length=100)  #attributes
    email=models.EmailField(max_length=20)
    contact=models.CharField(max_length=50)
    city=models.CharField(max_length=10)

class users(models.Model):
    fullname=models.CharField(max_length=100)  #attributes
    email=models.EmailField(max_length=20)
    contact=models.CharField(max_length=50)
    city=models.CharField(max_length=10)

class members(models.Model):
    fullname=models.CharField(max_length=100)  #attributes
    email=models.EmailField(max_length=20)
    contact=models.CharField(max_length=50)
    city=models.CharField(max_length=10)

class heroes(models.Model):
    fullname=models.CharField(max_length=100)  #attributes
    email=models.EmailField(max_length=20)
    contact=models.CharField(max_length=50)
    city=models.CharField(max_length=10)

class register(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=20)
    password=models.EmailField(max_length=6)
    contact=models.CharField(max_length=50)