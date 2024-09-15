from models.models import Recipe, MachineType

iron_ore = Recipe(
    recipe_name="Iron Ore",
    item_name="Iron Ore",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

copper_ore = Recipe(
    recipe_name="Copper Ore",
    item_name="Copper Ore",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

coal = Recipe(
    recipe_name="Coal",
    item_name="Coal",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

caterium_ore = Recipe(
    recipe_name="Caterium Ore",
    item_name="Caterium Ore",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

sulphur = Recipe(
    recipe_name="Sulphur",
    item_name="Sulphur",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

uranium_ore = Recipe(
    recipe_name="Uranium Ore",
    item_name="Uranium Ore",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

sam = Recipe(
    recipe_name="SAM Ore",
    item_name="SAM Ore",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

water = Recipe(
    recipe_name="Water",
    item_name="Water",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

iron_ingot = Recipe(
    recipe_name="Iron Ingot",
    item_name="Iron Ingot",
    ingredients={iron_ore: 30},
    output_per_minute=30,
    machine_type=MachineType.smelter,
)

copper_ingot = Recipe(
    recipe_name="Copper Ingot",
    item_name="Copper Ingot",
    ingredients={copper_ore: 30},
    output_per_minute=30,
    machine_type=MachineType.smelter,
)

pure_iron_ingot = Recipe(
    recipe_name="Pure Iron Ingot",
    item_name="Iron Ingot",
    ingredients={iron_ore: 35, water: 20},
    output_per_minute=65,
    machine_type=MachineType.refinery,
)

iron_alloy_ingot = Recipe(
    recipe_name="Iron Alloy Ingot",
    item_name="Iron Ingot",
    ingredients={iron_ore: 20, copper_ore: 20},
    output_per_minute=50,
    machine_type=MachineType.foundry,
)

iron_plate = Recipe(
    recipe_name="Iron Plate",
    item_name="Iron Plate",
    ingredients={iron_ingot: 30},
    output_per_minute=20,
    machine_type=MachineType.constructor,
)

iron_rod = Recipe(
    recipe_name="Iron Rod",
    item_name="Iron Rod",
    ingredients={iron_ingot: 15},
    output_per_minute=15,
    machine_type=MachineType.constructor,
)

screw = Recipe(
    recipe_name="Screw",
    item_name="Screw",
    ingredients={iron_rod: 10},
    output_per_minute=40,
    machine_type=MachineType.constructor,
)

steel_ingot = Recipe(
    recipe_name="Steel Ingot",
    item_name="Steel Ingot",
    ingredients={iron_ore: 45, coal: 45},
    output_per_minute=45,
    machine_type=MachineType.foundry,
)

solid_steel_ingot = Recipe(
    recipe_name="Solid Steel Ingot",
    item_name="Steel Ingot",
    ingredients={iron_ingot: 40, coal: 40},
    output_per_minute=60,
    machine_type=MachineType.foundry,
)

steel_beam = Recipe(
    recipe_name="Steel Beam",
    item_name="Steel Beam",
    ingredients={steel_ingot: 60},
    output_per_minute=15,
    machine_type=MachineType.constructor,
)

steel_pipe = Recipe(
    recipe_name="Steel Pipe",
    item_name="Steel Pipe",
    ingredients={steel_ingot: 30},
    output_per_minute=20,
    machine_type=MachineType.constructor,
)

wire = Recipe(
    recipe_name="Wire",
    item_name="Wire",
    ingredients={copper_ingot: 15},
    output_per_minute=30,
    machine_type=MachineType.constructor,
)

iron_wire = Recipe(
    recipe_name="Iron Wire",
    item_name="Wire",
    ingredients={iron_ingot: 12.5},
    output_per_minute=22.5,
    machine_type=MachineType.constructor,
)

reinforced_iron_plate = Recipe(
    recipe_name="Reinforced Iron Plate",
    item_name="Reinforced Iron Plate",
    ingredients={iron_plate: 30, screw: 60},
    output_per_minute=5,
    machine_type=MachineType.assembler,
)

stitched_iron_plate = Recipe(
    recipe_name="Stitched Iron Plate",
    item_name="Reinforced Iron Plate",
    ingredients={iron_plate: 18.75, wire: 37.5},
    output_per_minute=5.625,
    machine_type=MachineType.assembler,
)

cable = Recipe(
    recipe_name="Cable",
    item_name="Cable",
    ingredients={wire: 60},
    output_per_minute=30,
    machine_type=MachineType.constructor,
)

copper_sheet = Recipe(
    recipe_name="Copper Sheet",
    item_name="Copper Sheet",
    ingredients={copper_ingot: 20},
    output_per_minute=10,
    machine_type=MachineType.constructor,
)

caterium_ingot = Recipe(
    recipe_name="Caterium Ingot",
    item_name="Caterium Ingot",
    ingredients={caterium_ore: 45},
    output_per_minute=15,
    machine_type=MachineType.smelter,
)

caterium_wire = Recipe(
    recipe_name="Caterium Wire",
    item_name="Caterium Wire",
    ingredients={caterium_ingot: 12},
    output_per_minute=60,
    machine_type=MachineType.constructor,
)

stator = Recipe(
    recipe_name="Stator",
    item_name="Stator",
    ingredients={steel_pipe: 15, wire: 40},
    output_per_minute=5,
    machine_type=MachineType.assembler,
)

rotor = Recipe(
    recipe_name="Rotor",
    item_name="Rotor",
    ingredients={iron_rod: 20, screw: 100},
    output_per_minute=4,
    machine_type=MachineType.assembler,
)

steel_rotor = Recipe(
    recipe_name="Rotor",
    item_name="Steel Rotor",
    ingredients={steel_pipe: 10, wire: 30},
    output_per_minute=5,
    machine_type=MachineType.assembler,
)

motor = Recipe(
    recipe_name="Motor",
    item_name="Motor",
    ingredients={rotor: 10, stator: 10},
    output_per_minute=5,
    machine_type=MachineType.assembler,
)
