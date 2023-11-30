import json
import requests
from bs4 import BeautifulSoup
import re

# json_file_path = './recipes/appetizer_recipes.json'
json_file_path = ['./recipes/baked_goods_recipes.json','./recipes/breakfast_recipes.json','./recipes/condiments_recipes.json','./recipes/dessert_recipes.json','./recipes/sides_recipes.json','./recipes/soup_and_salad_recipes.json']

for json_file_path in json_file_path:

    # Open the JSON file for reading
    with open(json_file_path, 'r') as json_file:
        # Load the JSON data
        data = json.load(json_file)

    # Now, 'data' contains the content of the JSON file as a Python data structure
    # You can access and manipulate the data as needed
    for recipe in data:
            
        base_url = recipe['recipe-link']
        
        url = f'{base_url}'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36'} 
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        summary_container = soup.find('header', class_='wprm-entry-header')
        summary = summary_container.find('div', class_='wprm-recipe-summary')
    
        
        if summary_container:
            if summary and summary.text:
                print(summary.text)
                new_key = 'summary'
                new_data = summary.text
                recipe[new_key] = new_data

                with open(json_file_path, 'w') as json_file:
                    json.dump(data, json_file, indent=4)

                print('Summary added')
            else:
                print('No summary found or summary is empty. No changes made.')
        else:
            print('No summary container found. No changes made.')


                    
    print('ALL FINISHED')