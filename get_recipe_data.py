import json
import requests
import re
from bs4 import BeautifulSoup


json_file_path = "./prototype/prototype_recipes1.json"

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
        ", minced",
        ", about 12 to 15 feet",
        " to taste",
        ",  peeled and minced",
        ", chopped",
        ", cooked and removed from shell ",
        ", chopped",
        "(12 ounces) ",
        " (about 2 ½ cups), peeled and chopped",
        ", peeled and sliced thinly",
        ", shredded",
        "homemade ",
        " guisado, drained well",
        ", cored, seeded, and chopped",
        "cold, ",
        "thick-cut ",
        ", chopped",
        "small ",
        ", peeled and chopped",
        ", lightly beaten",
        "thumb-size ",
        ", pounded",
        "(19 ounces each) ",
        "Thai ",
        ", minced",
        "thumb-size ",
        ", peeled and grated",
        "(13.5 ounces) ",
        ", peeled and sliced",
        ", peeled and diced",
        "frozen ",
        ", thawed",
        ", beaten",
        ", tied into a knot",
        "(12 ounces each) ",
        ", peeled and minced",
        ", well beaten",
        ", deboned and flaked",
        ", thinly sliced",
        ", melted",
        ", sliced thinly",
        ", beaten ",
        "boneless, skinless ",
        " or leg meat",
        " peeled and sliced thinly",
        ", peeled and finely chopped",
        " (reserved from cooking the chicken)",
        ", diluted in 1 tablespoon water",
        ", peeled and quartered",
        "baby ",
        ", butterflied, gutted and deboned",
        ", peeled and crushe",
        ", cracked",
        " or leg meat, boneless and skinless",
        ", sliced to ¼-inch thick",
        ", boneless and skinless",
        "red food coloring",
        "(11.5 ounces) corned beef, chunky-style",
        "(11.5  ounces) ",
        " (about 2 ½ cups)",
    ]


for recipe in data:
    base_url = recipe["recipe-link"]

    url = f"{base_url}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    def get_recipe_summary(res):
        soup = BeautifulSoup(res.text, "html.parser")
        return (
            soup.find("div", class_="entry-content single-entry-content").find("p").text
        )

    summary = get_recipe_summary(response)
    # print(summary)
    # print()

    def get_recipe_ingredients(res):
        soup = BeautifulSoup(res.text, "html.parser")
        recipe_array = []

        ingredients_list = soup.find("ul", class_="wprm-recipe-ingredients")

        for ingredient in ingredients_list.find_all(
            "li", class_="wprm-recipe-ingredient"
        ):
            ingredient_name = ingredient.find(
                "span", class_="wprm-recipe-ingredient-name"
            )

            if ingredient_name:
                if ingredient_name.text not in ingredients_array:
                    recipe_array.append(ingredient_name.text)

        return recipe_array

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

    #     return final_array

    # filtered_ingredients = filter_ingredients(
    #     get_recipe_ingredients(response), filter_array
    # )

    # save_to_json(filtered_ingredients, "prototype_ingredients.json")

    filtered_proto = "./prototype/prototype_ingredients.json"

    def partial_match(word, sentence):
        return word in sentence

    def match_ingredients(sentences, word_array):
        matching_words = []
        for sentence in sentences:
            for word in word_array:
                if partial_match(word, sentence):
                    matching_words.append(word)
        return matching_words

    def read_json_file(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    filter_array_test = read_json_file(filtered_proto)

    result = match_ingredients(get_recipe_ingredients(response), filter_array_test)
    print(recipe["title"])
    print(result)

    def json_dump(path, key, key_data):
        new_key = key
        new_data = key_data
        recipe[new_key] = new_data

        with open(path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

    json_dump(json_file_path, "summary", summary)
    json_dump(json_file_path, "ingredients", result)
