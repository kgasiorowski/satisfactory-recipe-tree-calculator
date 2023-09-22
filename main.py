import models


if __name__ == "__main__":
    recipes = models.recipe_registry
    for item_name, recipes in recipes.items():
        for recipe in recipes:
            print(recipe.recipename(), recipe.ingredients())

    print(models.PureIronIngot.calculate_requirements_for_rate(300))
    print(models.IronIngot.calculate_requirements_for_rate(300))
