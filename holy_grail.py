import json
import requests
import re
from bs4 import BeautifulSoup


def GET_SUMMARY():
    json_file_path = "./prototype/prototype_appetizers_recipes.json"

    # Open the JSON file for reading
    with open(json_file_path, "r") as json_file:
        # Load the JSON data
        data = json.load(json_file)

        def json_dump(path, key, key_data):
            new_key = key
            new_data = key_data
            recipe[new_key] = new_data

            with open(path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4)

        def get_recipe_summary(res):
            soup = BeautifulSoup(res.text, "html.parser")
            return (
                soup.find("div", class_="entry-content single-entry-content")
                .find("p")
                .text
            )

    for recipe in data:
        base_url = recipe["recipe-link"]

        url = f"{base_url}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        summary = get_recipe_summary(response)

        json_dump(json_file_path, "summary", summary)


def GET_INGREDIENTS():

    json_file_path = "./prototype/prototype_appetizers_recipes.json"

    # Open the JSON file for reading
    with open(json_file_path, "r") as json_file:
        # Load the JSON data
        data = json.load(json_file)

        ingredients_array = []
        final_array = []

        ingredients_array = []
        final_array = []

        filter_array = [
            "(chinese parsley)",
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
            ", cut into 1-inch cubes",
            ", seeded and chopped",
            "juice of 1 ",
            "large ",
            "medium ",
            ", cut into pieces between bones",
            "head ",
            ", crushed",
            ", sliced to 1-inch wide and \u00bc-inch thick",
            "ground ",
            "(siling labuyo)",
            "(16 to 20 pieces) ",
            "ice ",
            ", hard-boiled and peeled",
            "(8 grams or about 1 \u00bd teaspoons) ",
            "orange food coloring powder or ",
            "(about 4 pieces) ",
            "(2 sticks) ",
            " (tuna) steaks, cut into 1-inch cubes",
            ", crushed",
            ", toasted",
            "fresh ",
            ", cooked",
            "seedless ",
            " (eden or velveeta), cut into \u00bc-inch x 3-inch strips",
            ", finely chopped",
        ]

        def save_to_json(data, filename):
            with open(filename, "w") as json_file:
                json.dump(data, json_file, indent=2)

        def json_dump(path, key, key_data):
            new_key = key
            new_data = key_data
            recipe[new_key] = new_data

            with open(path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4)

        def get_recipe_ingredients(res):
            soup = BeautifulSoup(res.text, "html.parser")
            recipe_array = []

            ingredients_container = soup.find(
                "div", class_="wprm-recipe-ingredients-container"
            )

            # Find all list items within the container
            ingredients_list = ingredients_container.find_all(
                "li", class_="wprm-recipe-ingredient"
            )

            # Print the text content of each ingredient
            for ingredient in ingredients_list:

                recipe_array.append(ingredient.text.strip())

            return recipe_array

        # def filter_ingredients(data, filters):
        #     for ingr in data:
        #         ingr_name = ingr
        #         for word in filters:
        #             ingr_name = ingr_name.replace(word, "")
        #         if ingr_name not in final_array:
        #             final_array.append(ingr_name.lower())

        #     return final_array

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

    for recipe in data:
        base_url = recipe["recipe-link"]

        url = f"{base_url}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36"
        }

        response = requests.get(url, headers=headers)

        filtered_proto = "./all_ingredients/all_ingredients.json"
        filter_array_test = read_json_file(filtered_proto)
        result = match_ingredients(get_recipe_ingredients(response), filter_array_test)

        print(recipe["title"])
        print(result)
        print()

        json_dump(json_file_path, "ingredients", result)


def GET_INSTRUCTION():
    json_file_path = "./prototype/prototype_appetizers_recipes.json"

    # Open the JSON file for reading
    with open(json_file_path, "r") as json_file:
        # Load the JSON data
        data = json.load(json_file)

        def json_dump(path, key, key_data):
            new_key = key
            new_data = key_data
            recipe[new_key] = new_data

            with open(path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4)

        print("ALL FINISHED")

        def get_recipe_instruction(res):
            soup = BeautifulSoup(res.text, "html.parser")
            instruction = soup.find("ul", class_="wprm-recipe-instructions").findAll(
                "li"
            )

            instructionArray = []

            for i in instruction:
                span_element = i.find("div").find("span")
                if span_element:
                    instructionArray.append(span_element.text)

            return instructionArray

    for recipe in data:
        base_url = recipe["recipe-link"]

        url = f"{base_url}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        instruction = get_recipe_instruction(response)
        json_dump(json_file_path, "instruction", instruction)


def GET_INGREDIENT_LIST():
    json_file_path = "./prototype/prototype_appetizers_recipes.json"

    # Open the JSON file for reading
    with open(json_file_path, "r") as json_file:
        # Load the JSON data
        data = json.load(json_file)

        def json_dump(path, key, key_data):
            new_key = key
            new_data = key_data
            recipe[new_key] = new_data

            with open(path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4)

        print("ALL FINISHED")

        def ingredientList(res):
            soup = BeautifulSoup(res.text, "html.parser")
            ingredient_list = soup.find("ul", class_="wprm-recipe-ingredients").findAll(
                "li"
            )

            ingrListArray = []  # Initialize an empty list to store sentences

            for i in ingredient_list:
                span_elements = i.findAll("span")

                # Iterate over the found span elements and get their text content
                span_list = [span.text for span in span_elements]

                # Join the text content of span elements into a single sentence
                sentence = " ".join(span_list)

                ingrListArray.append(sentence)  # Append the sentence to the list

            return ingrListArray

        # print(all_ingredients)

    for recipe in data:
        base_url = recipe["recipe-link"]

        url = f"{base_url}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        all_ingredients = ingredientList(response)

        json_dump(json_file_path, "ingredientList", all_ingredients)


def GET_SERVING():
    json_file_path = "./prototype/prototype_appetizers_recipes.json"

    # Open the JSON file for reading
    with open(json_file_path, "r") as json_file:
        # Load the JSON data
        data = json.load(json_file)

        def json_dump(path, key, key_data):
            new_key = key
            new_data = key_data
            recipe[new_key] = new_data

            with open(path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4)

        def get_recipe_summary(res):
            soup = BeautifulSoup(res.text, "html.parser")
            return (
                soup.find("div", class_="entry-content single-entry-content")
                .find("p")
                .text
            )

        def get_recipe_serving(res):

            soup = BeautifulSoup(res.text, "html.parser")
            return (
                soup.find("span", class_="wprm-recipe-servings-with-unit")
                .find("span")
                .text
            )

    for recipe in data:
        base_url = recipe["recipe-link"]

        url = f"{base_url}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        serving = get_recipe_serving(response)

        json_dump(json_file_path, "serving", serving)
