from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    CATEGORY_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Comfort Food', 'Comfort Food'),
        ('Quick and Easy', 'Quick and Easy'),
        ('Low Carb', 'Low Carb'),
        ('Salads', 'Salads'),
        ('Desserts', 'Desserts'),
        ('Drinks', 'Drinks'),
    ]

    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.IntegerField(help_text="Preparation time in minutes")
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(
        upload_to='recipe_images/', null=True, blank=True, verbose_name='Recipe Image')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return self.name
