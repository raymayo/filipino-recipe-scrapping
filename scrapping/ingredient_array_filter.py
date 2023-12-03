import json
import requests
import re
from colorama import init, Fore

new_array = []

ingredient_path = './appetizer_test.json'
with open(ingredient_path, 'r') as ingredient_file:

    data = json.load(ingredient_file)
    
for ingr in data:
    # Initialize an empty list for each ingredient
    result_array = []

    # Check if 'or' is present
    if 'or' in ingr:
        remove_or = ingr.split(' or ')
        result_array += [value.strip() for value in remove_or if value.strip() != '']

    # Check if 'and' is present
    if 'and' in ingr:
        remove_and = ingr.split(' and ')
        result_array += [value.strip() for value in remove_and if value.strip() != '']

    # If neither 'or' nor 'and' is present, add the original ingredient
    if not ('or' in ingr or 'and' in ingr):
        result_array.append(ingr.strip())

    new_array += result_array
    
    if ingr not in new_array:
        new_array.append(ingr)
        new_array.sort()

with open('appetizer_test2.json', 'w') as json_file:
    json.dump(new_array, json_file, indent=4)

print(Fore.RED + 'ALL INGREDIENTS HAVE BEEN SAVED!!!')
