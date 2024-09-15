from models.models import Recipe, MachineType

iron_ore = Recipe(
    recipe_name="Iron Ore",
    item_name="Iron Ore",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw
)

copper_ore = Recipe(
    recipe_name="Copper Ore",
    item_name="Copper Ore",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw
)

water = Recipe(
    recipe_name="Water",
    item_name="Water",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw
)

iron_ingot = Recipe(
    recipe_name="Iron Ingot",
    item_name="Iron Ingot",
    ingredients={iron_ore: 30},
    output_per_minute=30,
    machine_type=MachineType.smelter
)

copper_ingot = Recipe(
    recipe_name="Copper Ingot",
    item_name="Copper Ingot",
    ingredients={copper_ore: 30},
    output_per_minute=30,
    machine_type=MachineType.smelter
)

pure_iron_ingot = Recipe(
    recipe_name="Pure Iron Ingot",
    item_name="Iron Ingot",
    ingredients={iron_ore: 35, water: 20},
    output_per_minute=65,
    machine_type=MachineType.refinery
)

iron_alloy_ingot = Recipe(
    recipe_name="Iron Alloy Ingot",
    item_name="Iron Ingot",
    ingredients={iron_ore: 20, copper_ore: 20},
    output_per_minute=50,
    machine_type=MachineType.foundry
)
