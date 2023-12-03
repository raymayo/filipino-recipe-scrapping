import re
import json

json_recipe = ["./recipes/appetizer_recipes.json", "./recipes/appetizer_recipes.json"]

# Read JSON data from file
with open("data.json", "r") as file:
    data = json.load(file)


# Define a function to remove units using regex
def remove_units(value):
    return re.sub(r"[^\d.]", "", value)


# Apply the function to each value in the "nutritions" section
for key, value in data["nutritions"].items():
    data["nutritions"][key] = remove_units(value)

# Write the modified data back to the file
with open("modified_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Modified data has been written to 'modified_data.json'.")
