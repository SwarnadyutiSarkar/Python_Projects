import requests
from bs4 import BeautifulSoup
import random

def scrape_allrecipes():
    url = 'https://www.allrecipes.com/recipes/'
    response = requests.get(url)
    
    if response.status_code != 200:
        print('Failed to retrieve data')
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    recipe_links = []
    
    # Find recipe links on the page
    for link in soup.find_all('a', {'class': 'card__titleLink'}):
        recipe_links.append(link.get('href'))
    
    return recipe_links

def scrape_recipe(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print('Failed to retrieve data')
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    ingredients = []
    
    # Find ingredients on the page
    for ingredient in soup.find_all('span', {'class': 'ingredients-item-name'}):
        ingredients.append(ingredient.text.strip())
    
    return ingredients

def generate_recipe(recipe_links):
    random_recipe_url = random.choice(recipe_links)
    ingredients = scrape_recipe(random_recipe_url)
    
    return ingredients

# Scrape recipe links from Allrecipes.com
recipe_links = scrape_allrecipes()

# Generate a new recipe
new_recipe = generate_recipe(recipe_links)
print("Generated Recipe:")
for ingredient in new_recipe:
    print(ingredient)
