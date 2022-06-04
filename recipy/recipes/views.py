from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.

posts = [
    {'author': 'RR',
     'title': 't',
     'content': 'content1',
     'date_posted': 'dd'},
    {'author': 'RR',
     'title': 't',
     'content': 'content1',
     'date_posted': 'dd'},
    {'author': 'RR',
     'title': 't',
     'content': 'content1',
     'date_posted': 'dd'}
]

# class HomeView(TemplateView):
#     template_name = 'home/'


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'recipes/home.html', context)
