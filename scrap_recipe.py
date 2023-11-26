import json
import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Your User Agent'}

base_url = 'https://www.kawalingpinoy.com/category/spreads-sauces-and-condiments/page/'
page_number = 1  # Start from the first page
all_recipes = []  # To store recipes from all pages

# while page_number <= 1: 
while page_number <= 25:
    url = f'{base_url}{page_number}/'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        recipe_container = soup.find('main', id='genesis-content')
        
        recipe_article = recipe_container.find_all('header', class_='entry-header')

        for article in recipe_article:
            current_page_recipes = []

            recipe_titles = article.find_all('h2', class_='entry-title')
            image_src = article.find_all('img')
            a_tag = article.find_all('a', class_='entry-image-link')

            for title in recipe_titles:
                print(f"Title: {title.text}")
                
                for a in a_tag:

                    for image in image_src:
                        if not image['src'].startswith('data:image/svg+xml'):

                            current_page_recipes.append({
                                'title': title.text,
                                'recipe-link' : a['href'],
                                'image': image['src'],
                                'meal': 'condiment'
                            })

            all_recipes.extend(current_page_recipes)

        page_number += 1
    else:
        print(f"Error: {response.status_code}")
        break

# Save all recipes to a JSON file
with open('condiments_recipes.json', 'w') as json_file:
    json.dump(all_recipes, json_file, indent=4)

