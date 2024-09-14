import pydantic
import abc
import enum


class BaseModel(pydantic.BaseModel, abc.ABC):
    ...


class MachineType(enum.Enum):
    constructor = 4
    assembler = 15
    smelter = 4
    foundry = 16
    refinery = 30


class Recipe(BaseModel):
    name: str
    output_per_minute: int
    ingredients: list[tuple["Item", int]]
    machine: MachineType
    byproduct: tuple[str, int] | None = None


class Item(BaseModel):
    name: str = "default"
    recipes: list[Recipe] | None = None


water = Item(name="Water")
iron_ore = Item(name="Iron Ore")
iron_ingot = Item(
    name="Iron Ingot",
    recipes=[
        Recipe(
            name="default",
            output_per_minute=30,
            ingredients=[(iron_ore, 30)],
            machine=MachineType.smelter,
        ),
        Recipe(
            name="Pure Iron Ingot",
            output_per_minute=65,
            ingredients=[(iron_ore, 35), (water, 20)],
            machine=MachineType.refinery,
        ),
    ],
)
