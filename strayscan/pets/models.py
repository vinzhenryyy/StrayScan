from django.db import models

class PetLog(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]

    pet_name = models.CharField(max_length=100, blank=True, null=True)
    pet_type = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    location = models.CharField(max_length=200)
    date = models.DateField()
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pet_name or 'Unnamed'} ({self.status})"
