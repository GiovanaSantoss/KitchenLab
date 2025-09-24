# KitchenLab

KitchenLab is a personal recipe management web application built with Django and JavaScript. It allows users to create, view, and delete their own recipes, complete with images, ingredients, instructions, preparation time, difficulty levels, and categories. The application is mobile-responsive and provides an interactive experience for users to explore their recipes efficiently.

## Features

- User authentication with login and logout.
- Add new recipes with image upload.
- View recipe details, including ingredients and instructions.
- Delete recipes (only by the user who created them).
- Mobile-responsive layout with a grid of recipe cards.
- Interactive recipe cards that expand to show details when clicked.
- Minimalist and visually clean UI for easy navigation and readability.

## Distinctiveness and Complexity

KitchenLab stands out from other projects in the CS50W course because it is neither a social network nor a typical e-commerce site. Instead, it is a personal culinary management system that integrates several advanced concepts:

- Backend powered by Django, with a `Recipe` model that stores detailed information about each recipe.
- Frontend interactivity using JavaScript to expand and collapse recipe details dynamically.
- Image handling with file uploads.
- User-specific actions: recipes can only be deleted by their creators.
- Mobile-responsive design using CSS Grid and media queries.
- Validations and form handling using Django forms and CSRF protection.

The project demonstrates the complexity of integrating backend and frontend technologies while maintaining a user-friendly interface and ensuring data integrity.

## File Structure

- `recipes/` - Django app containing models, views, templates, and static files.
  - `models.py` - Defines the `Recipe` model.
  - `views.py` - Contains all view functions including listing, adding, and deleting recipes.
  - `urls.py` - URL routing for the recipes app.
  - `templates/recipes/` - HTML templates for listing and adding recipes.
  - `static/recipes/style.css` - CSS for styling the pages.
- `KitchenLab/` - Django project configuration files.
- `manage.py` - Django management script.
- `requirements.txt` - Lists required Python packages (Django, Pillow).

## Installation and Running

1. Clone the repository:

```bash
git clone https://github.com/GiovanaSantoss/KitchenLab.git
cd KitchenLab
````
2. Create a virtual environment and activate it:

````
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
````
3. Install dependencies:

```
pip install -r requirements.txt
```
4. Apply database migrations:
   
```
python manage.py migrate
```
5. Create a superuser to manage recipes (optional):

```
python manage.py createsuperuser
```
6. Run the development server:

```
python manage.py runserver
```

7. Open your browser and navigate to http://127.0.0.1:8000/ to access KitchenLab.

   ## Additional Information

-- Images uploaded are stored in the media/recipe_images/ directory.

-- Recipes are only deletable by the user who created them.

-- The recipe details section is hidden by default and revealed using JavaScript when a recipe card is clicked.

-- The layout adapts to different screen sizes using CSS Grid and media queries for a better mobile experience.
