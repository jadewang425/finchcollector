from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    breed = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.breed
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
