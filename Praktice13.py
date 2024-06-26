# Darbs ar JSON API
# 1a. Izvelciet 5 receptes kas satur kartupeļus no sekojoša API:
# https://dummyjson.com/recipes
# Dati jasaglabā .json failā bet arī jaizveido python datu struktūra
# PS. ASV izrunā kartupeli kā potato :)
import json
import requests
# function to search recipe by ingredient
def search(ingredient):
    search_result = []
    for p in parsed_recipes:
        ingredient_string = str(p['ingredients']).lower()
        if ingredient_string.__contains__(ingredient.lower()):
            search_result.append(p)
    return search_result

url = "https://dummyjson.com/recipes"
response = requests.get(url)
if response.status_code == 200:
    data = response.json() # download json data
    parsed_recipes = data['recipes'] # parce recipes from JSON
    for p in parsed_recipes:
        print (p['id'], p['mealType'])
    with open('parsed_recipes.json', 'w',encoding="utf-8") as f:
        json.dump(parsed_recipes, f) # Save all recipes to JSON file
    # take first 5 Potato containing recipes (if there are so much)
    potato_recipes = search("Potato")[:4]
    with open('potato_recipes.json', 'w',encoding="utf-8") as f: 
        json.dump(potato_recipes, f, indent=4) # Save Potato recipes to JSON file
else:
    print(f"Status code is {response.status_code}")
    # raise Exception("API did not return 200 status code")
# 1b. Izvelciet  visas  zupu receptes no tā API
# Te var būt dažādi piegājieni, bet visticamāk mūs interesēs mealType lauks kurā ir viena no vērtībām soup

