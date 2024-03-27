from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Other, dispatch_uid='create_complaint_from_specific')
@receiver(post_save, sender=RapeComplaint, dispatch_uid='create_complaint_from_specific')
@receiver(post_save, sender=SexualMisconductComplaint, dispatch_uid='create_complaint_from_specific')
@receiver(post_save, sender=HarassmentComplaint, dispatch_uid='create_complaint_from_specific')

def create_complaint_from_specific(sender, instance, created, **kwargs):
    if created:
        Complaint.objects.get_or_create(
            category=instance.category, 
            date=instance.date,
            location=instance.location,
            description=instance.description,
            evidence=instance.evidence,
            email=instance.email

        )

@receiver(post_save, sender=Complaint, dispatch_uid='create_specific_complaint')
def create_specific_complaint(sender, instance, created, **kwargs):
    if created:
        if instance.category=='rape':
            RapeComplaint.objects.get_or_create(
            category='rape',
            date=instance.date,
            location=instance.location,
            description=instance.description,
            evidence=instance.evidence,
            email=instance.email
        )
        elif instance.category=='other':
            Other.objects.get_or_create(
            category='bullying',
            date=instance.date,
            location=instance.location,
            description=instance.description,
            evidence=instance.evidence,
            email=instance.email
        )
        elif instance.category=='sexual_misconduct':
            SexualMisconductComplaint.objects.get_or_create(
            category='sexual_misconduct',
            date=instance.date,
            location=instance.location,
            description=instance.description,
            evidence=instance.evidence,
            email=instance.email
        )
            
        elif instance.category=='harassment':
            HarassmentComplaint.objects.get_or_create(
            category='harassment',
            date=instance.date,
            location=instance.location,
            description=instance.description,
            evidence=instance.evidence,
            email=instance.email
        )