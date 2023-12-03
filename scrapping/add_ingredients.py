import json
import requests
from bs4 import BeautifulSoup
import re
from colorama import init, Fore

all_array = []  

def is_exact_word_present(sentence, word):
    words = sentence.split()
    return any(word.lower() == w.lower() for w in words)


json_file_path = './test.json'
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
    
all_ingredients_path = './appetizer_test3.json'
with open(all_ingredients_path, 'r') as all_ingredients:
    all_ingredients = json.load(all_ingredients)

 
for recipe in data:
    
    ingredient_array = []
        
    base_url = recipe['recipe-link']
    
    url = f'{base_url}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36'} 
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('section', class_='wprm-entry-content')
    
    ingredients_container = container.findAll('ul', class_='wprm-recipe-ingredients');

                
                            
                            
    for ul in ingredients_container:
        the_ingredients = ul.find_all('li', class_='wprm-recipe-ingredient')

        for ingr in the_ingredients:
            ingr_name = ingr.find('span', class_='wprm-recipe-ingredient-name').text.lower().strip().split(',')
            new_name = ingr_name[0].strip()
            
            print(new_name)
            for checked_ingredient in all_ingredients:

                    if new_name == checked_ingredient:

                        print(f"The exact word '{checked_ingredient}' is present in the sentence.")
                        
                        # Assuming you meant to use 'checked_ingredient' instead of 'active_ingredient'
                        if checked_ingredient not in ingredient_array:
                            ingredient_array.append(checked_ingredient)

        json_key = 'ingredients'
        json_data = ingredient_array
        recipe[json_key] = json_data

        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)


            
print(Fore.RED + 'ALL INGREDIENTS HAVE BEEN SAVED!!!')

        
