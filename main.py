from _legacy_models import Item, Recipe
import models
from pprint import pprint
import json


def load_alt_selections():
    with open("alts.json", "r") as alts_json:
        return json.load(alts_json)


def load_recipes():
    flat_recipe_map = {}

    with open("recipes.json", "r") as raw_file:
        raw_recipe_json = json.load(raw_file)

    try:
        # Load all the recipes first
        for item in raw_recipe_json:
            newItem = Item()
            newItem.name = item["name"]
            if "recipes" in item and item["recipes"] is not None:
                for recipeName, recipeData in item["recipes"].items():
                    newRecipe = Recipe()
                    newRecipe.name = recipeName
                    newRecipe.output_per_minute = recipeData["output_per_minute"]
                    newRecipe.ingredients = recipeData["inputs"]
                    newRecipe.machine = (
                        recipeData["machine"] if "machine" in recipeData else "machine"
                    )
                    if "byproduct" in recipeData:
                        newRecipe.byproduct = list(recipeData["byproduct"].items())[0]
                    newItem.recipes.append(newRecipe)
            flat_recipe_map[newItem.name] = newItem

        for item in flat_recipe_map.values():
            if item.recipes is not None:
                temp_recipes = {}
                for recipe in item.recipes:
                    temp_ingredient_list = []
                    for ingredient, amount in recipe.ingredients.items():
                        temp_ingredient_list.append(
                            (flat_recipe_map[ingredient], amount)
                        )
                    recipe.ingredients = temp_ingredient_list
                    temp_recipes[recipe.name] = recipe
                item.recipes = temp_recipes

    except Exception as e:
        print(f"There was an error loading data for item {newItem.name}")
        print(e)
        exit()

    return flat_recipe_map


def print_recipe(
        item: Item, amount_per_minute: float, alts: dict = None, skipped_items: list = None
):
    # alts = alts if alts is not None else load_alt_selections()
    alts = {**load_alt_selections(), **alts}
    base_ingredient_amounts = {}

    power_dict = {
        "Assemblers": 15,
        "Smelters": 4,
        "Constructors": 4,
        "Refineries": 30,
        "Manufacturers": 55,
        "Foundries": 16,
        "Particle Accelerators": 1000,
        "Blenders": 75,
    }
    total_power_consumption = 0

    def __print_recipe_recurs(item: Item, amount_per_minute: float, tabnum: int):
        tabstring = "".join(["\t" for _ in range(tabnum)])
        strang = f"{tabstring}{item.name} - {round(amount_per_minute, 4)} pm"

        recipe = None
        if item.recipes:
            recipe = item.recipes["default"]

            if item.name in alts:
                recipe = item.recipes[alts[item.name]]

            strang += f" - {round(amount_per_minute / recipe.output_per_minute, 2)} {recipe.machine}"

            if recipe.machine in power_dict:
                nonlocal total_power_consumption
                total_power_consumption += (
                        round(amount_per_minute / recipe.output_per_minute, 2)
                        * power_dict[recipe.machine]
                )

        print(strang)

        if skipped_items is not None and item.name in skipped_items:
            base_ingredient_amounts.setdefault(item.name, 0)
            base_ingredient_amounts[item.name] += amount_per_minute
            return

        if recipe is not None:
            for ingredient in recipe.ingredients:
                __print_recipe_recurs(
                    ingredient[0],
                    (amount_per_minute * (ingredient[1] / recipe.output_per_minute)),
                    tabnum + 1,
                )
        else:
            base_ingredient_amounts.setdefault(item.name, 0)
            base_ingredient_amounts[item.name] += amount_per_minute

    __print_recipe_recurs(item, amount_per_minute, 0)

    base_ingredient_amounts = {
        **{key: round(value, 4) for key, value in base_ingredient_amounts.items()},
        "total_power_consumption": total_power_consumption,
    }

    return base_ingredient_amounts


recipes = load_recipes()

if __name__ == "__main__":
    # pprint(
    #     print_recipe(
    #         recipes["High-Speed Connector"],
    #         40,
    #         alts={
    #             "High-Speed Connector": "Silicon High-Speed Connector",
    #             "Circuit Board": "Silicon Circuit Board",
    #         },
    #     )
    # )

    pprint(models.iron_ingot.model_dump())
    ...
