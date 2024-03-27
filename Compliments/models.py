from django.db import models

# Create your models here.
class Compliment(models.Model):
    compliment = models.CharField(max_length=255)
    reason = models.TextField()

    def __str__(self) -> str:
        return f"{self.compliment}"
    
