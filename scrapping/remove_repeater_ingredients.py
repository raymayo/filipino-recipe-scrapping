import json
import requests
from bs4 import BeautifulSoup
import re
from colorama import init, Fore

all_ingredients = []

with open("./appetizer_test2.json", "r") as file:
    # Load the JSON array
    data = json.load(file)
    
    for ingredient in data:
        
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
            all_ingredients.sort()
            
            with open('appetizer_test3.json', 'w') as json_file:
                json.dump(all_ingredients, json_file, indent=4)
                    
print(Fore.RED + 'ALL INGREDIENTS HAVE BEEN SAVED!!!')


