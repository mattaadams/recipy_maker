from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Recipe


# class HomeView(TemplateView):
#     template_name = 'home/'


def home(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'recipes/home.html', context)
