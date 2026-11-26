from django.shortcuts import render
from django.http import Http404
from .recipe_data import RECIPES


CATEGORIES = {
    "cakes": "Cakes",
    "pastries": "Pastries",
    "bread": "Bread",
    "savouries": "Savouries",
    "african-snacks": "African Snacks",
    "cookies": "Cookies",
    "desserts": "Desserts",
}


def home(request):
    return render(request, "recipes/home.html")


def category(request, category_slug):

    if category_slug not in CATEGORIES:
        raise Http404("Category not found")

    category_recipes = [
        recipe for recipe in RECIPES
        if recipe["category"] == category_slug
    ]

    context = {
        "category_name": CATEGORIES[category_slug],
        "recipes": category_recipes,
    }

    return render(request, "recipes/category.html", context)


def recipe_detail(request, recipe_slug):

    recipe = next(
        (item for item in RECIPES
         if item["slug"] == recipe_slug),
        None
    )

    if recipe is None:
        raise Http404("Recipe not found")

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe}
    )


def about(request):
    return render(request, "recipes/about.html")


def contact(request):
    return render(request, "recipes/contact.html")