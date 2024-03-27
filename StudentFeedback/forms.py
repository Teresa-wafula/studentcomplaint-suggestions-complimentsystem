from django import forms
from .models import *


class ComplaintForm(forms.ModelForm):
    date=forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    class Meta:
        model = Complaint
        fields = ("email","category", "date", "location", "evidence", "description", )

# 