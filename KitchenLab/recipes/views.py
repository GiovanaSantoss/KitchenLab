from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm

from django.contrib.auth.decorators import login_required


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})
