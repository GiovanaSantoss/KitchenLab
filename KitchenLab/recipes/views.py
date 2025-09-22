from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


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



@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.created_by == request.user:  # só o dono pode deletar
        recipe.delete()
    return redirect('index')