import json
import requests
from bs4 import BeautifulSoup
import re

# headers = {'User-Agent': 'Your User Agent'}

# base_url = 'https://www.kawalingpinoy.com/category/spreads-sauces-and-condiments/page/'
# page_number = 1  # Start from the first page
# all_recipes = []  # To store recipes from all pages

# # while page_number <= 1: 
# while page_number <= 25:
#     url = f'{base_url}{page_number}/'
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         recipe_container = soup.find('main', id='genesis-content')
        
#         recipe_article = recipe_container.find_all('header', class_='entry-header')

#         for article in recipe_article:
#             current_page_recipes = []

#             recipe_titles = article.find_all('h2', class_='entry-title')
#             image_src = article.find_all('img')
#             a_tag = article.find_all('a', class_='entry-image-link')

#             for title in recipe_titles:
#                 print(f"Title: {title.text}")
                
#                 for a in a_tag:

#                     for image in image_src:
#                         if not image['src'].startswith('data:image/svg+xml'):

#                             current_page_recipes.append({
#                                 'title': title.text,
#                                 'recipe-link' : a['href'],
#                                 'image': image['src'],
#                                 'meal': 'condiment'
#                             })

#             all_recipes.extend(current_page_recipes)

#         page_number += 1
#     else:
#         print(f"Error: {response.status_code}")
#         break

# # Save all recipes to a JSON file
# with open('condiments_recipes.json', 'w') as json_file:
#     json.dump(all_recipes, json_file, indent=4)








# json_file_path = './recipes/soup_and_salad_recipes.json'

# # Open the JSON file for reading
# with open(json_file_path, 'r') as json_file:
#     # Load the JSON data
#     data = json.load(json_file)

# # Now, 'data' contains the content of the JSON file as a Python data structure
# # You can access and manipulate the data as needed
# for recipe in data:
        
#     base_url = recipe['recipe-link']
    
#     url = f'{base_url}'
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36'} 
#     response = requests.get(url, headers=headers)
#     print(response)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     nutrion_container = soup.find('div', class_='wprm-nutrition-label-container')
    
#     # Check if nutrion_container exists
#     if nutrion_container:
#         nutrions = nutrion_container.find_all('span', class_='wprm-nutrition-label-text-nutrition-container')
        
#         nutrition_dict = {}
#         nutrition_array = []

#         for nutrion in nutrions:
#             # Split the text into key and value based on the colon
#             key, value = map(str.strip, nutrion.text.split(':'))

#             # Store the key-value pair in the dictionary
#             nutrition_dict[key] = value

#         # Specify the keys you're interested in
#         keys_of_interest = ['Calories', 'Carbohydrates', 'Protein', 'Fat', 'Saturated Fat', 'Polyunsaturated Fat', 'Monounsaturated Fat', 'Cholesterol', 'Sodium', 'Potassium', 'Fiber', 'Sugar', 'Vitamin A', 'Vitamin C', 'Calcium', 'Iron']

#         # Print the relevant information
#         for key in keys_of_interest:
#             if key in nutrition_dict:
#                 print(f"{key}: {nutrition_dict[key]}")
#                 new_key = 'nutrions'
#                 new_data = nutrition_dict
#                 recipe[new_key] = new_data
                
#                 with open(json_file_path, 'w') as json_file:
#                     json.dump(data, json_file, indent=4)
#             else:
#                 print(f"{key} not found in the nutrition information.\n")
#     else:
#         print("Nutrition information not found.\n")







# # json_file_path = './test.json'
# json_file_path = './recipes/appetizer_recipes.json'

# # Open the JSON file for reading
# with open(json_file_path, 'r') as json_file:
#     # Load the JSON data
#     data = json.load(json_file)

# # Now, 'data' contains the content of the JSON file as a Python data structure
# # You can access and manipulate the data as needed
# for recipe in data:
        
#     base_url = recipe['recipe-link']
    
#     url = f'{base_url}'
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36'} 
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     container = soup.find('article', class_='status-publish')
#     ingredients_container = container.find_all('ul');
    
#     if len(ingredients_container) >= 2:
#         second_result = ingredients_container[2]
#         ingredients = second_result.find_all('li')
        
#         ingredient_array = []
        
#         for ingr in ingredients :
            
#             ingr_name = ingr.text.split('-')
#             name_sorted = ingr_name[0].lower().split(', ')
            
#             for name in name_sorted :
#                 print()
                
#                 ingredient_array += name.split(' and ')
            
#             # print(ingredient_array)
            
#             # ingredient_array.append(name_sorted.lower())
#                 new_key = 'ingredients'
#                 new_data = ingredient_array
#                 recipe[new_key] = new_data
                
#                 print(ingredient_array)
                
#                 with open(json_file_path, 'w') as json_file:
#                     json.dump(data, json_file, indent=4)
                    
#                     print('all saved')
        
#     elif  len(ingredients_container) == 1 :
#         print("RESULT IS SHORT")   
#     else:
#         print("Not enough results")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
