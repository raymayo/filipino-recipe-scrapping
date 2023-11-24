import json

# Read the JSON file
json_file_path = './test.json'
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Insert a new key-value pair into each dictionary in the list
new_key = 'new_key'
new_value = ['hello', 123]

for item in data:
    item[new_key] = new_value

# Write the updated data structure back to the JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Added key '{new_key}' with value '{new_value}' to each dictionary in {json_file_path}")
