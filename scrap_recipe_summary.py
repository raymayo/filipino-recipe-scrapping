import json
import requests
from bs4 import BeautifulSoup
import re

json_file_path = './recipes/beverage_recipes.json'

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
    print(summary.text)
    
    if summary_container:
        new_key = 'summary'
        new_data = summary.text
        recipe[new_key] = new_data
        
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)