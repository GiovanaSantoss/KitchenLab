from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

import requests
from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})


@login_required
def add_recipe(request):
    dog_image_url = None
    saved = False

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()

            response = requests.get('https://dog.ceo/api/breeds/image/random')
            data = response.json()
            dog_image_url = data['message']
            saved = True

            form = RecipeForm()
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {
        'form': form,
        'dog_image_url': dog_image_url,
        'saved': saved
    })


@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.created_by == request.user:
        recipe.delete()
    return redirect('index')


@csrf_exempt
def rate_recipe(request, recipe_id):
    if request.method == "POST":
        data = json.loads(request.body)
        rating = int(data.get("rating", 0))
        recipe = Recipe.objects.get(id=recipe_id)
        recipe.rating = rating
        recipe.save()
        return JsonResponse({"success": True, "rating": rating})
    return JsonResponse({"success": False}, status=400)
