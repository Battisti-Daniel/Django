from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe

def home(request):
    return render(request,"recipes/pages/home.html", context={
        'recipes': [make_recipe() for i in range(10)],
    })

def recipe(request,id):
    return render(request,"recipes/pages/home-view.html", context={
        'recipe': make_recipe(),
        "is_datail_page" : True,
    })

