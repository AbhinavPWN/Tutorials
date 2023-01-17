from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)


class Review(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(30)])


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} teaches {self.subject}"
