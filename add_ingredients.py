import json
import requests
from bs4 import BeautifulSoup
import re
from colorama import init, Fore

all_array = []  

json_file_path = './recipes/dessert_recipes.json'


with open(json_file_path, 'r') as json_file:

    data = json.load(json_file)
    
 
for recipe in data:
        
    base_url = recipe['recipe-link']
    
    url = f'{base_url}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36'} 
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('section', class_='wprm-entry-content')
    

    
    ingredients_container = container.findAll('ul', class_='wprm-recipe-ingredients');
    
    pattern = r'\([^)]*\) '
    
    ingredient_array = []
    
    
    for ul in ingredients_container :
        ingredients = ul.findAll('li', class_='wprm-recipe-ingredient')
        
        for ingr in ingredients:
            ingr_name = ingr.text.lower()
            print(ingr_name)
    
