from django.db import models
class Category(models.Model ):
    name = models.CharField(max_length=20,null=False,blank=True,unique=True)

class Student(models.Model ):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=100,null=False,blank=True,unique=True)

class Teacher(models.Model ):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))

    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    address = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"