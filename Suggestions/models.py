from django.db import models

# Create your models here.
class Suggestion(models.Model):
    CATEGORY_CHOICES=[
        ('academic', 'Academic Program Enhancements'),
        ('infrastructure', 'Campus Facilities and Infrastructure'),
        ('outreach', 'Community Engagement and Outreach'),
        ('technology', 'Technology and Digital Resources'),
        ('others', 'Others'),
    ]
    category= models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description=models.TextField()
    solution=models.CharField(max_length=255)

    def __str__(self):
        return self.category


class AcademicSuggestions(Suggestion):
    class Meta:
        verbose_name="Academic Program Enhancement"
        verbose_name_plural="Academic Program Enhancements"

class InfrastructureSuggestion(Suggestion):
    class Meta:
        verbose_name="Cammpus Facilities and Infrustructure"
        verbose_name_plural="Cammpus Facilities and Infrustructure"

class TechnologySuggestion(Suggestion):
    class Meta:
        verbose_name="Technology and Digital Resources"
        verbose_name_plural="Technology and Digital Resources"

class OutreachSuggetion(Suggestion):
    class Meta:
        verbose_name="Community Engagement and Outreach"
        verbose_name_plural="Community Engagement and Outreach"

class OtherSuggetions(Suggestion):
    class Meta:
        verbose_name="Other Suggetion"
        verbose_name_plural="Other Suggetions"