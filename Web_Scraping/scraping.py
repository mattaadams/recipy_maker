import pandas as pd
from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

article = soup.find('article')

print(article.h2.a.text)
