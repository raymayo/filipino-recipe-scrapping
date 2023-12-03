import json
import requests
from bs4 import BeautifulSoup
import re
from colorama import init, Fore

all_array = []


def scrap_nutrients():
    base_url = recipe["recipe-link"]

    url = f"{base_url}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    nutrion_container = soup.find("div", class_="wprm-nutrition-label-container")
    # print(nutrion_container)

    if nutrion_container:
        nutrions = nutrion_container.find_all(
            "span", class_="wprm-nutrition-label-text-nutrition-container"
        )

        nutrition_dict = {}
        nutrition_array = []

        for nutrion in nutrions:
            # Split the text into key and value based on the colon
            key, value = map(str.strip, nutrion.text.split(":"))

            # Store the key-value pair in the dictionary
            nutrition_dict[key] = value

        # Specify the keys you're interested in
        keys_of_interest = [
            "Calories",
            "Carbohydrates",
            "Protein",
            "Fat",
            "Saturated Fat",
            "Polyunsaturated Fat",
            "Monounsaturated Fat",
            "Cholesterol",
            "Sodium",
            "Potassium",
            "Fiber",
            "Sugar",
            "Vitamin A",
            "Vitamin C",
            "Calcium",
            "Iron",
        ]

        # Print the relevant information
        for key in keys_of_interest:
            if key in nutrition_dict:
                print(f"{key}: {nutrition_dict[key]}")
                new_key = "nutrions"
                new_data = nutrition_dict
                recipe[new_key] = new_data

                with open(json_file_path, "w") as json_file:
                    json.dump(data, json_file, indent=4)
            else:
                print(f"{key} not found in the nutrition information.\n")
    else:
        print("Nutrition information not found.\n")


def scrap_ingredients():
    base_url = recipe["recipe-link"]

    url = f"{base_url}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.find("section", class_="wprm-entry-content")

    ingredients_container = container.findAll("ul", class_="wprm-recipe-ingredients")

    ingredient_array = []

    print(recipe["recipe-link"])
    for ul in ingredients_container:
        ingredients = ul.findAll("li", class_="wprm-recipe-ingredient")

        for ingr in ingredients:
            ingr_name = (
                ingr.find("span", class_="wprm-recipe-ingredient-name")
                .text.lower()
                .strip()
            )
            result_name = re.sub(r"\([^)]*\)", "", ingr_name).strip().split(",")
            new_ingr = result_name[0].rstrip().split("to taste")
            all_array.append(new_ingr[0])
            print(new_ingr[0])

        print()


def is_exact_word_present(sentence, word):
    words = sentence.split()
    return any(word.lower() == w.lower() for w in words)


json_file_path = "./recipes/appetizer_recipes.json"
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

all_ingredients_path = "./all_ingredients/all_ingredients.json"
with open(all_ingredients_path, "r") as all_ingredients:
    all_ingredients = json.load(all_ingredients)


for recipe in data:
    scrap_nutrients()
    # scrap_ingredients()
