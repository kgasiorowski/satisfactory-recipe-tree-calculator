import abc
from typing import Dict, Type, Any
from enum import Enum
import pydantic


class BaseModel(pydantic.BaseModel):
    ...


class MachineType(Enum):
    constructor = 4
    assembler = 15
    smelter = 4
    foundry = 16
    refinery = 30
    manufacturer = 55
    raw = 0


AlternateRecipes = Dict[Type["Recipe"], Type["Recipe"]]


class Recipe(BaseModel, abc.ABC):
    product_name: str
    recipe_name: str
    output_per_minute: float | None
    ingredients: dict["Recipe", float] | None
    machine_type: MachineType

    # would be handy to use these as dict keys so here we go
    def __hash__(self):
        return int.from_bytes(self.recipe_name.encode(), "little")

    def calculate_requirements_for_rate(
            self,
            rate: float,
            alts: AlternateRecipes = {},
            print_tree: bool = False,
            num_tabs: int = 0,
            skipped_items: list[str] = [],
    ) -> (dict[str, int], float):
        # Check if this recipe needs to be substituted
        recipe = alts[self] if self in alts else self

        # Keep track of needed items and power requirements
        required_ingredients = dict()
        total_power_required = 0.0

        # Skip these calculations if the recipe is for a raw resource
        if recipe.output_per_minute is not None:
            num_machines = round(rate / recipe.output_per_minute, 6)
            recipe_power_required = int(recipe.machine_type.value) * num_machines
            total_power_required += recipe_power_required

        if print_tree:
            output = f"{recipe.product_name} - {round(rate, 6)}"
            if recipe.output_per_minute is not None:
                output += f" - {num_machines} {recipe.machine_type.name.capitalize()}(s) - {total_power_required} MW"
            print(("\t" * num_tabs) + output)

        # Base case. Return immediately if its a raw resource
        if recipe.ingredients is None or recipe in skipped_items:
            return {recipe.product_name: rate}, 0

        # Recursively get the required items and power
        for ingredient, quantity in recipe.ingredients.items():
            # fmt: off
            sub_results, sub_power_required = ingredient.calculate_requirements_for_rate(
                rate=(rate / recipe.output_per_minute * quantity),
                alts=alts,
                num_tabs=num_tabs + 1,
                print_tree=print_tree,
                skipped_items=skipped_items,
            )
            # fmt: on
            for base_ingredient, base_ingredient_rate in sub_results.items():
                required_ingredients.setdefault(base_ingredient, 0)
                required_ingredients[base_ingredient] += base_ingredient_rate
            total_power_required += sub_power_required
        return required_ingredients, total_power_required
