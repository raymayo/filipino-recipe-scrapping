import json
import requests
from bs4 import BeautifulSoup
import re

json_file_path = './recipes/soup_and_salad_recipes.json'

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
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    nutrion_container = soup.find('div', class_='wprm-nutrition-label-container')
    
    # Check if nutrion_container exists
    if nutrion_container:
        nutrions = nutrion_container.find_all('span', class_='wprm-nutrition-label-text-nutrition-container')
        
        nutrition_dict = {}
        nutrition_array = []

        for nutrion in nutrions:
            # Split the text into key and value based on the colon
            key, value = map(str.strip, nutrion.text.split(':'))

            # Store the key-value pair in the dictionary
            nutrition_dict[key] = value

        # Specify the keys you're interested in
        keys_of_interest = ['Calories', 'Carbohydrates', 'Protein', 'Fat', 'Saturated Fat', 'Polyunsaturated Fat', 'Monounsaturated Fat', 'Cholesterol', 'Sodium', 'Potassium', 'Fiber', 'Sugar', 'Vitamin A', 'Vitamin C', 'Calcium', 'Iron']

        # Print the relevant information
        for key in keys_of_interest:
            if key in nutrition_dict:
                print(f"{key}: {nutrition_dict[key]}")
                new_key = 'nutrions'
                new_data = nutrition_dict
                recipe[new_key] = new_data
                
                with open(json_file_path, 'w') as json_file:
                    json.dump(data, json_file, indent=4)
            else:
                print(f"{key} not found in the nutrition information.\n")
    else:
        print("Nutrition information not found.\n")
