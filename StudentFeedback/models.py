# complaints/models.py
from django.db import models
from django.utils import timezone
class BaseComplaint(models.Model):
    CATEGORY_CHOICES = [
        ('rape', 'Rape Complaint'),
        ('sexual_misconduct', 'Sexual Misconduct Complaint'),
        ('other', 'Other Complaint'),
        ('harassment', 'Harassment Complaint'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    description = models.TextField()
    evidence = models.FileField(blank=False, null=False)
    email= models.EmailField()

    def __str__(self):
        return f"{self.get_category_display()} - {self.description}"
    
    class Meta:
        abstract=True

class Complaint(BaseComplaint):
    pass

class RapeComplaint(BaseComplaint):
    def save(self, *args,  **kwargs):
        self.category='rape'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'Rape Complaint - {self.description}'

   

class SexualMisconductComplaint(BaseComplaint):
    def save(self, *args,  **kwargs):
        self.category='sexual_misconduct'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'Sexual Misconduct ComplaintRape Complaint - {self.description}'

class Other(BaseComplaint):
        def save(self, *args,  **kwargs):
            self.category='other'
            super().save(*args, **kwargs)
        
        def __str__(self):
            return f'Other Complaint - {self.description}'

class HarassmentComplaint(BaseComplaint):
    def save(self, *args,  **kwargs):
            self.category='harassment'
            super().save(*args, **kwargs)
        
    def __str__(self):
        return f'Harassment Complaint - {self.description}'


class Student(models.Model):

    fullname=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    password1=models.CharField(max_length=255)
    password2=models.CharField(max_length=255)

    def __str__(self):
        return self.fullname
