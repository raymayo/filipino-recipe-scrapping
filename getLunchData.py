import json
import requests
from bs4 import BeautifulSoup
import re

base_url = "https://www.kawalingpinoy.com/category/main-dishes/page/"
page_number = 1  # Start from the first page
all_recipes = []  # To store recipes from all pages


while page_number <= 25:
    url = f"{base_url}{page_number}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    recipe_container = soup.find("main", id="genesis-content")
    recipe = recipe_container.findAll("article", class_="status-publish")

    for recipe in recipe:
        current_recipes = []
        recipe_title = recipe["aria-label"]
        recipe_link = recipe.find("a", class_="entry-title-link")["href"]
        recipe_image = recipe.findAll("img", class_="entry-image")
        for image in recipe_image:
            if not image["src"].startswith("data:image/svg+xml"):
                image_src = image["src"]

                current_recipes.append(
                    {
                        "title": recipe_title,
                        "recipe-link": recipe_link,
                        "image": image_src,
                        "meal": "main dish",
                    }
                )

        all_recipes.extend(current_recipes)
    page_number += 1

    with open("prototype_main_recipes.json", "w", encoding="utf-8") as json_file:
        json.dump(all_recipes, json_file, indent=4, ensure_ascii=False)
print("ALL FINISHED")
