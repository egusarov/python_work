from django.shortcuts import render

from .models import Meal

def index(request):
    """The home page for Meal Planner."""
    return render(request, 'meal_plans/index.html')