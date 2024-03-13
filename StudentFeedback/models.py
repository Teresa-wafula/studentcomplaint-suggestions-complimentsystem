# complaints/models.py
from django.db import models
from django.utils import timezone
class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('rape', 'Rape Complaint'),
        ('sexual_misconduct', 'Sexual Misconduct Complaint'),
        ('bullying', 'Bullying Complaint'),
        ('harassment', 'Harassment Complaint'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    description = models.TextField()
    evidence = models.FileField(upload_to='uploads/', blank=False, null=False)

    def __str__(self):
        return f"{self.get_category_display()} - {self.description}"

class RapeComplaint(Complaint):
    class Meta:
        verbose_name = "Rape Complaint"
        verbose_name_plural = "Rape Complaints"

class SexualMisconductComplaint(Complaint):
    class Meta:
        verbose_name = "Sexual Misconduct Complaint"
        verbose_name_plural = "Sexual Misconduct Complaints"

class BullyingComplaint(Complaint):
    class Meta:
        verbose_name = "Bullying Complaint"
        verbose_name_plural = "Bullying Complaints"

class HarassmentComplaint(Complaint):
    class Meta:
        verbose_name = "Harassment Complaint"
        verbose_name_plural = "Harassment Complaints"

class Student(models.Model):

    fullname=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    password1=models.CharField(max_length=255)
    password2=models.CharField(max_length=255)

    def __str__(self):
        return self.fullname
