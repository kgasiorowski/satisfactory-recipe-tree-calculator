import abc
from typing import Dict, List, Type

class Recipe(abc.ABC):
    __default_recipe__: bool = False
    __itemname__: str
    __recipename__: str
    __output_per_minute__: int | None
    __ingredients__: Dict[str, int] | None

    @classmethod
    def itemname(cls):
        return cls.__itemname__

    @classmethod
    def recipename(cls):
        return cls.__recipename__

    @classmethod
    def output_per_minute(cls):
        return cls.__output_per_minute__

    @classmethod
    def ingredients(cls):
        return cls.__ingredients__


class IronOre(Recipe):
    __recipename__ = "Iron Ore"
    __itemname__ = "Iron Ore"
    __ingredients__ = None
    __output_per_minute__ = None


class CopperOre(Recipe):
    __recipename__ = "Copper Ore"
    __itemname__ = "Copper Ore"
    __ingredients__ = None
    __output_per_minute__ = None


class IronIngot(Recipe):
    __recipename__ = "Iron Ingot"
    __itemname__ = "Iron Ingot"
    __ingredients__ = {"Iron Ore": 30}
    __output_per_minute__ = 30


class CopperIngot(Recipe):
    __recipename__ = "Copper Ingot"
    __itemname__ = "Copper Ingot"
    __ingredients__ = {"Copper Ore": 30}
    __output_per_minute__ = 30


class Water(Recipe):
    __recipename__ = "Water"
    __itemname__ = "Water"
    __ingredients__ = None
    __output_per_minute__ = None


class PureIronIngot(Recipe):
    __recipename__ = "Pure Iron Ingot"
    __itemname__ = "Iron Ingot"
    __ingredients__ = {"Iron Ore": 35, "Water": 20}
    __output_per_minute__ = 50


RecipeRegistry = Dict[str, List[Type[Recipe]]]


def _create_recipe_registry() -> RecipeRegistry:
    g = {k: v for k, v in globals().items()}
    r: RecipeRegistry = {}
    for v in g.values():
        if isinstance(v, type) and issubclass(v, Recipe) and v.__name__ != Recipe.__name__:
            if v.__itemname__ not in r:
                r[v.__itemname__] = [v]
            else :
                r[v.__itemname__].append(v)
    return r

recipe_registry = _create_recipe_registry()
