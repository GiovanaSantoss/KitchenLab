from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'instructions',
                  'prep_time', 'difficulty', 'category', 'image']
        widgets = {
            'rating': forms.Select(choices=[(i, f"{i} Stars") for i in range(1, 6)])
        }