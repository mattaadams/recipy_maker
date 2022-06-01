import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

MAIN_STRING = "carouselNav__list elementFont__resetList recipeCarousel__list"  # class for main recipe category page navlist
CAT_STRING = "category-page-list-content category-page-list-content__recipe-card karma-main-column"  # Class for category page div
CARDS_STRING = "card__titleLink manual-link-behavior elementFont__title margin-8-bottom"  # Class for most popular recipe cards


def get_links():
    source = requests.get('https://www.allrecipes.com/recipes/').text
    soup = BeautifulSoup(source, 'lxml')
    recipe_list = soup.find('ul', class_=MAIN_STRING)

    links = []
    pop_recipes = []
    for a in recipe_list.find_all('a', href=True):
        links.append(a['href'])
        for i, _ in enumerate(links):
            recipe_category = requests.get(links[i]).text
            cat_soup = BeautifulSoup(recipe_category, 'lxml')  # category page
            most_CARDS = cat_soup.find('div', class_=CAT_STRING)
            for a in most_CARDS.find_all('a', class_=CARDS_STRING, href=True):
                if re.search('https://www.allrecipes.com/recipe/.*', a['href']):
                    pop_recipes.append(a['href'])

    df = pd.DataFrame(pop_recipes, columns=["link"])
    df.to_csv('list.csv', index=False)
    return df
