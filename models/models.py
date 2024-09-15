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
    raw = 0


AlternateRecipes = Dict[Type["Recipe"], Type["Recipe"]]


class Recipe(BaseModel, abc.ABC):
    item_name: str
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
    ) -> dict[str, int]:
        if print_tree:
            output = f"{self.item_name} - {rate}"
            if self.output_per_minute is not None:
                output += f" - {round(rate / self.output_per_minute, 6)} {self.machine_type.name.capitalize()}(s)"
            print(("\t" * num_tabs) + output)

        if self.ingredients is None:
            return {self.item_name: rate}
        required_ingredients = dict()
        for ingredient, quantity in self.ingredients.items():
            # The recipe for the ingredient could be an alt so check that here
            ingredient = alts[ingredient] if ingredient in alts else ingredient
            sub_results = ingredient.calculate_requirements_for_rate(
                rate=(rate / self.output_per_minute * quantity),
                alts=alts,
                num_tabs=num_tabs + 1,
                print_tree=print_tree,
            )
            for base_ingredient, base_ingredient_rate in sub_results.items():
                required_ingredients.setdefault(base_ingredient, 0)
                required_ingredients[base_ingredient] += base_ingredient_rate
        return required_ingredients
