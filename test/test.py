import requests
from bs4 import BeautifulSoup

url = "https://www.kawalingpinoy.com/chizza/"

# Set headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send an HTTP request to the URL
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the container for recipe ingredients
    ingredients_container = soup.find("div", class_="wprm-recipe-ingredients-container")

    # Find all list items within the container
    ingredients_list = ingredients_container.find_all(
        "li", class_="wprm-recipe-ingredient"
    )

    # Print the text content of each ingredient
    for ingredient in ingredients_list:
        print(ingredient.text.strip())
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
