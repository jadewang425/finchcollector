from django.db import models
from django.urls import reverse

from datetime import date

# define a tuple of 2-tuples for MEALS
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.color} {self.name}"
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'toy_id': self.id})

# Create your models here.
class Finch(models.Model):
    breed = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    # add the M:M relationship
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.breed
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

# Add Feeding model
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    # Create a cat_id FK
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']