import json
import requests
import re
from bs4 import BeautifulSoup


json_file_path = "./prototype/prototype_recipes.json"

# Open the JSON file for reading
with open(json_file_path, "r") as json_file:
    # Load the JSON data
    data = json.load(json_file)

    # Now, 'data' contains the content of the JSON file as a Python data structure
    # You can access and manipulate the data as needed

    ingredients_array = []
    final_array = []

    filter_array = [
        ", peeled and minced",
        "cold, cooked ",
        "thumb-size ",
        ", peeled and grated",
        "large ",
        " peeled and diced",
        ", peeled and chopped",
        "dark ",
        ", thinly sliced",
        "boneless, skinless ",
        " or leg meat",
        "baby ",
        ", butterflied, gutted and deboned",
        ", sliced to ¼-inch thick",
        "cold ",
        "small ",
    ]


for recipe in data:
    base_url = recipe["recipe-link"]

    url = f"{base_url}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    # def get_recipe_summary(res):
    #     soup = BeautifulSoup(res.text, "html.parser")
    #     return soup.find("div", class_="wprm-recipe-summary").find("span").text

    # summary = get_recipe_summary(response)
    # print(summary)
    # print()

    def get_recipe_ingredients(res):
        soup = BeautifulSoup(res.text, "html.parser")

        ingredients_list = soup.find("ul", class_="wprm-recipe-ingredients")

        for ingredient in ingredients_list.find_all(
            "li", class_="wprm-recipe-ingredient"
        ):
            # Find the span element within each li element
            ingredient_name = ingredient.find(
                "span", class_="wprm-recipe-ingredient-name"
            )

            # Check if the span element is found before appending to the list
            if ingredient_name:
                if ingredient_name.text not in ingredients_array:
                    ingredient_name.text.strip().split(" or ")
                    ingredients_array.append(ingredient_name.text)
                    print(ingredients_array)
                    # print()

                    # return ingredients_array

        # Assuming 'response' is defined elsewhere in your code

    def save_to_json(data, filename):
        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent=2)

    # def filter_ingredients(data, filters):
    #     for ingr in data:
    #         ingr_name = ingr
    #         for word in filters:
    #             ingr_name = ingr_name.replace(word, "")
    #         if ingr_name not in final_array:
    #             final_array.append(ingr_name)
    #             return final_array

    # # Apply the filter
    # filtered_ingredients = filter_ingredients(
    #     get_recipe_ingredients(response), filter_array
    # )

    # save_to_json(filtered_ingredients, "prototype_ingredients.json")

    # get_recipe_ingredients(response)

    # save_to_json(get_recipe_ingredients(response), "prototype_ingredients.json")

    ingre_list = get_recipe_ingredients(response)
