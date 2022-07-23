import requests

recipe_list = requests.get('http://127.0.0.1:8000/api/recipes/')
