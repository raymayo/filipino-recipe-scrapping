import json
import requests
import re
from bs4 import BeautifulSoup


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
        instruction = soup.find("ul", class_="wprm-recipe-instructions").findAll("li")

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
