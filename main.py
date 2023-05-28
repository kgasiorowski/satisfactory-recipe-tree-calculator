import models
from models import Recipe
from pprint import pprint
import json


# def load_alt_selections():
#     with open('alts.json', 'r') as alts_json:
#         return json.load(alts_json)
#
#
# def load_recipes():
#     flat_recipe_map = {}
#
#     with open('recipes.json', 'r') as raw_file:
#         raw_recipe_json = json.load(raw_file)
#
#     try:
#         # Load all the recipes first
#         for item in raw_recipe_json:
#             newItem = Item()
#             newItem.name = item['name']
#             if 'recipes' in item and item['recipes'] is not None:
#                 for recipeName, recipeData in item['recipes'].items():
#                     newRecipe = Recipe()
#                     newRecipe.name = recipeName
#                     newRecipe.output_per_minute = recipeData['output_per_minute']
#                     newRecipe.ingredients = recipeData['inputs']
#                     newItem.recipes.append(newRecipe)
#             flat_recipe_map[newItem.name] = newItem
#
#         for item in flat_recipe_map.values():
#             if item.recipes is not None:
#                 temp_recipes = {}
#                 for recipe in item.recipes:
#                     temp_ingredient_list = []
#                     for ingredient, amount in recipe.ingredients.items():
#                         temp_ingredient_list.append((flat_recipe_map[ingredient], amount))
#                     recipe.ingredients = temp_ingredient_list
#                     temp_recipes[recipe.name] = recipe
#                 item.recipes = temp_recipes
#
#     except Exception as e:
#         print(f"There was an error loading data for item {newItem.name}")
#         print(e)
#         exit()
#
#     return flat_recipe_map
#
#
# def print_recipe(item: Item, amount_per_minute: float, alts: dict=None, skipped_items: list=None):
#     alts = alts if alts is not None else load_alt_selections()
#     base_ingredient_amounts = {}
#
#     def __print_recipe_recurs(item: Item, amount_per_minute: float, tabnum: int):
#
#         tabstring = ''.join(['\t' for _ in range(tabnum)])
#         print(f"{tabstring}{item.name} - {round(amount_per_minute, 4)} pm")
#
#         if skipped_items is not None and item.name in skipped_items:
#             base_ingredient_amounts.setdefault(item.name, 0)
#             base_ingredient_amounts[item.name] += amount_per_minute
#             return
#
#         if item.recipes:
#             recipe = item.recipes['default']
#
#             if item.name in alts:
#                 recipe = item.recipes[alts[item.name]]
#             for ingredient in recipe.ingredients:
#                 __print_recipe_recurs(ingredient[0], amount_per_minute * (ingredient[1] / recipe.output_per_minute), tabnum+1)
#         else:
#             base_ingredient_amounts.setdefault(item.name, 0)
#             base_ingredient_amounts[item.name] += amount_per_minute
#
#     __print_recipe_recurs(item, amount_per_minute, 0)
#
#     for key in base_ingredient_amounts.keys():
#         base_ingredient_amounts[key] = round(base_ingredient_amounts[key], 4)
#
#     return base_ingredient_amounts


if __name__ == "__main__":
    # recipes = load_recipes()
    # pprint(print_recipe(
    #     recipes['Smart Plating'],
    #     60,
    #     skipped_items=["Rotor"]
    # ))

    print(models.recipe_registry)

