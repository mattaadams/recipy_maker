import pandas as pd
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.allrecipes.com/recipes/').text

soup = BeautifulSoup(source, 'lxml')

recipe_list = soup.find('ul', class_="carouselNav__list elementFont__resetList recipeCarousel__list")

links = []
for a in recipe_list.find_all('a', href=True):
    links.append(a['href'])

# print(links[0])

recipe_category = requests.get(links[0]).text

cat_soup = BeautifulSoup(recipe_category, 'lxml')
print(cat_soup.prettify())
