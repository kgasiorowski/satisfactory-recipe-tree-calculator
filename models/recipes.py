from models.models import Recipe, MachineType

iron_ore = Recipe(
    recipe_name="Iron Ore",
    product_name="Iron Ore",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

copper_ore = Recipe(
    recipe_name="Copper Ore",
    product_name="Copper Ore",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

coal = Recipe(
    recipe_name="Coal",
    product_name="Coal",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

caterium_ore = Recipe(
    recipe_name="Caterium Ore",
    product_name="Caterium Ore",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

sulphur = Recipe(
    recipe_name="Sulphur",
    product_name="Sulphur",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

uranium_ore = Recipe(
    recipe_name="Uranium Ore",
    product_name="Uranium Ore",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

sam = Recipe(
    recipe_name="SAM Ore",
    product_name="SAM Ore",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

water = Recipe(
    recipe_name="Water",
    product_name="Water",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

limestone = Recipe(
    recipe_name="Limestone",
    product_name="Limestone",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

concrete = Recipe(
    recipe_name="Concrete",
    product_name="Concrete",
    ingredients={limestone: 45},
    output_per_minute=15,
    machine_type=MachineType.constructor,
)

wet_concrete = Recipe(
    recipe_name="Wet Concrete",
    product_name="Concrete",
    ingredients={limestone: 120, water: 100},
    output_per_minute=80,
    machine_type=MachineType.refinery,
)

raw_quartz = Recipe(
    recipe_name="Raw Quartz",
    product_name="Raw Quartz",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

compacted_coal = Recipe(
    recipe_name="Compacted Coal",
    product_name="Compacted Coal",
    ingredients={coal: 25, sulphur: 25},
    output_per_minute=25,
    machine_type=MachineType.assembler,
)

polymer_resin_byproduct = Recipe(
    recipe_name="Polymer Resin Byproduct",
    product_name="Polymer Resin",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

crude_oil = Recipe(
    recipe_name="Crude Oil",
    product_name="Crude Oil",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

heavy_oil_residue_byproduct = Recipe(
    recipe_name="Heavy Oil Residue Byproduct",
    product_name="Heavy Oil Residue",
    ingredients=None,
    output_per_minute=None,
    machine_type=MachineType.raw,
)

rubber = Recipe(
    recipe_name="Rubber",
    product_name="Rubber",
    ingredients={crude_oil: 30, heavy_oil_residue_byproduct: -20},
    output_per_minute=20,
    machine_type=MachineType.refinery,
)

heavy_oil_residue = Recipe(
    recipe_name="Heavy Oil Residue",
    product_name="Heavy Oil Residue",
    ingredients={crude_oil: 30, polymer_resin_byproduct: -20},
    output_per_minute=40,
    machine_type=MachineType.refinery,
)

quartz_crystal = Recipe(
    recipe_name="Quartz Crystal",
    product_name="Quartz Crystal",
    ingredients={raw_quartz: 37.5},
    output_per_minute=22.5,
    machine_type=MachineType.constructor,
)

silica = Recipe(
    recipe_name="Silica",
    product_name="Silica",
    ingredients={raw_quartz: 22.5},
    output_per_minute=37.5,
    machine_type=MachineType.constructor,
)

iron_ingot = Recipe(
    recipe_name="Iron Ingot",
    product_name="Iron Ingot",
    ingredients={iron_ore: 30},
    output_per_minute=30,
    machine_type=MachineType.smelter,
)

copper_ingot = Recipe(
    recipe_name="Copper Ingot",
    product_name="Copper Ingot",
    ingredients={copper_ore: 30},
    output_per_minute=30,
    machine_type=MachineType.smelter,
)

pure_iron_ingot = Recipe(
    recipe_name="Pure Iron Ingot",
    product_name="Iron Ingot",
    ingredients={iron_ore: 35, water: 20},
    output_per_minute=65,
    machine_type=MachineType.refinery,
)

iron_alloy_ingot = Recipe(
    recipe_name="Iron Alloy Ingot",
    product_name="Iron Ingot",
    ingredients={iron_ore: 20, copper_ore: 20},
    output_per_minute=50,
    machine_type=MachineType.foundry,
)

iron_plate = Recipe(
    recipe_name="Iron Plate",
    product_name="Iron Plate",
    ingredients={iron_ingot: 30},
    output_per_minute=20,
    machine_type=MachineType.constructor,
)

iron_rod = Recipe(
    recipe_name="Iron Rod",
    product_name="Iron Rod",
    ingredients={iron_ingot: 15},
    output_per_minute=15,
    machine_type=MachineType.constructor,
)

screw = Recipe(
    recipe_name="Screw",
    product_name="Screw",
    ingredients={iron_rod: 10},
    output_per_minute=40,
    machine_type=MachineType.constructor,
)

steel_ingot = Recipe(
    recipe_name="Steel Ingot",
    product_name="Steel Ingot",
    ingredients={iron_ore: 45, coal: 45},
    output_per_minute=45,
    machine_type=MachineType.foundry,
)

cast_screw = Recipe(
    recipe_name="Cast Screw",
    product_name="Screw",
    ingredients={iron_ingot: 12.5},
    output_per_minute=50,
    machine_type=MachineType.constructor,
)

solid_steel_ingot = Recipe(
    recipe_name="Solid Steel Ingot",
    product_name="Steel Ingot",
    ingredients={iron_ingot: 40, coal: 40},
    output_per_minute=60,
    machine_type=MachineType.foundry,
)

steel_beam = Recipe(
    recipe_name="Steel Beam",
    product_name="Steel Beam",
    ingredients={steel_ingot: 60},
    output_per_minute=15,
    machine_type=MachineType.constructor,
)

steel_screw = Recipe(
    recipe_name="Steel Screw",
    product_name="Screw",
    ingredients={steel_beam: 5},
    output_per_minute=260,
    machine_type=MachineType.constructor,
)

molded_beam = Recipe(
    recipe_name="Molded Beam",
    product_name="Steel Beam",
    ingredients={steel_ingot: 120, concrete: 80},
    output_per_minute=45,
    machine_type=MachineType.assembler,
)

steel_pipe = Recipe(
    recipe_name="Steel Pipe",
    product_name="Steel Pipe",
    ingredients={steel_ingot: 30},
    output_per_minute=20,
    machine_type=MachineType.constructor,
)

wire = Recipe(
    recipe_name="Wire",
    product_name="Wire",
    ingredients={copper_ingot: 15},
    output_per_minute=30,
    machine_type=MachineType.constructor,
)

iron_wire = Recipe(
    recipe_name="Iron Wire",
    product_name="Wire",
    ingredients={iron_ingot: 12.5},
    output_per_minute=22.5,
    machine_type=MachineType.constructor,
)

reinforced_iron_plate = Recipe(
    recipe_name="Reinforced Iron Plate",
    product_name="Reinforced Iron Plate",
    ingredients={iron_plate: 30, screw: 60},
    output_per_minute=5,
    machine_type=MachineType.assembler,
)

stitched_iron_plate = Recipe(
    recipe_name="Stitched Iron Plate",
    product_name="Reinforced Iron Plate",
    ingredients={iron_plate: 18.75, wire: 37.5},
    output_per_minute=5.625,
    machine_type=MachineType.assembler,
)

bolted_iron_plate = Recipe(
    recipe_name="Bolted Iron Plate",
    product_name="Reinforced Iron Plate",
    ingredients={iron_plate: 90, screw: 250},
    output_per_minute=15,
    machine_type=MachineType.assembler,
)

adhered_iron_plate = Recipe(
    recipe_name="Adhered Iron Plate",
    product_name="Reinforced Iron Plate",
    ingredients={iron_plate: 11.25, rubber: 3.75},
    output_per_minute=3.75,
    machine_type=MachineType.assembler,
)

modular_frame = Recipe(
    recipe_name="Modular Frame",
    product_name="Modular Frame",
    ingredients={reinforced_iron_plate: 3, iron_rod: 12},
    output_per_minute=2,
    machine_type=MachineType.assembler,
)

bolted_frame = Recipe(
    recipe_name="Bolted Frame",
    product_name="Modular Frame",
    ingredients={reinforced_iron_plate: 7.5, screw: 140},
    output_per_minute=5,
    machine_type=MachineType.assembler,
)

steeled_frame = Recipe(
    recipe_name="Steeled Frame",
    product_name="Modular Frame",
    ingredients={reinforced_iron_plate: 2, steel_pipe: 10},
    output_per_minute=3,
    machine_type=MachineType.assembler,
)

cable = Recipe(
    recipe_name="Cable",
    product_name="Cable",
    ingredients={wire: 60},
    output_per_minute=30,
    machine_type=MachineType.constructor,
)

copper_sheet = Recipe(
    recipe_name="Copper Sheet",
    product_name="Copper Sheet",
    ingredients={copper_ingot: 20},
    output_per_minute=10,
    machine_type=MachineType.constructor,
)

caterium_ingot = Recipe(
    recipe_name="Caterium Ingot",
    product_name="Caterium Ingot",
    ingredients={caterium_ore: 45},
    output_per_minute=15,
    machine_type=MachineType.smelter,
)

caterium_wire = Recipe(
    recipe_name="Caterium Wire",
    product_name="Caterium Wire",
    ingredients={caterium_ingot: 12},
    output_per_minute=60,
    machine_type=MachineType.constructor,
)

stator = Recipe(
    recipe_name="Stator",
    product_name="Stator",
    ingredients={steel_pipe: 15, wire: 40},
    output_per_minute=5,
    machine_type=MachineType.assembler,
)

rotor = Recipe(
    recipe_name="Rotor",
    product_name="Rotor",
    ingredients={iron_rod: 20, screw: 100},
    output_per_minute=4,
    machine_type=MachineType.assembler,
)

steel_rotor = Recipe(
    recipe_name="Steel Rotor",
    product_name="Rotor",
    ingredients={steel_pipe: 10, wire: 30},
    output_per_minute=5,
    machine_type=MachineType.assembler,
)

motor = Recipe(
    recipe_name="Motor",
    product_name="Motor",
    ingredients={rotor: 10, stator: 10},
    output_per_minute=5,
    machine_type=MachineType.assembler,
)

smart_plating = Recipe(
    recipe_name="Smart Plating",
    product_name="Smart Plating",
    ingredients={reinforced_iron_plate: 2, rotor: 2},
    output_per_minute=2,
    machine_type=MachineType.assembler,
)

plastic = Recipe(
    recipe_name="Plastic",
    product_name="Plastic",
    ingredients={crude_oil: 30, heavy_oil_residue_byproduct: -10},
    output_per_minute=20,
    machine_type=MachineType.refinery,
)

plastic_smart_plating = Recipe(
    recipe_name="Plastic Smart Plating",
    product_name="Smart Plating",
    ingredients={reinforced_iron_plate: 2.5, rotor: 2.5, plastic: 7.5},
    output_per_minute=5,
    machine_type=MachineType.manufacturer,
)

fuel = Recipe(
    recipe_name="Fuel",
    product_name="Fuel",
    ingredients={crude_oil: 60, polymer_resin_byproduct: -30},
    output_per_minute=40,
    machine_type=MachineType.refinery,
)

residual_fuel = Recipe(
    recipe_name="Residual Fuel",
    product_name="Fuel",
    ingredients={heavy_oil_residue: 60},
    output_per_minute=40,
    machine_type=MachineType.refinery,
)

turbofuel = Recipe(
    recipe_name="Turbofuel",
    product_name="Turbofuel",
    ingredients={fuel: 22.5, compacted_coal: 15},
    output_per_minute=18.75,
    machine_type=MachineType.refinery,
)

turbo_heavy_fuel = Recipe(
    recipe_name="Turbo Heavy Fuel",
    product_name="Turbofuel",
    ingredients={heavy_oil_residue: 37.5, compacted_coal: 30},
    output_per_minute=30,
    machine_type=MachineType.refinery,
)

diluted_packaged_fuel = Recipe(
    recipe_name="Diluted Packaged Fuel",
    product_name="Fuel",
    ingredients={heavy_oil_residue: 30, water: 60},
    output_per_minute=60,
    machine_type=MachineType.refinery,
)

turbofuel_generator = Recipe(
    recipe_name="Turbofuel Generator",
    product_name="Turbofuel Generator",
    ingredients={turbofuel: 7.5},
    output_per_minute=1,
    machine_type=MachineType.raw,
)

turbofuel_generator_250 = Recipe(
    recipe_name="Turbofuel Generator",
    product_name="Turbofuel Generator",
    ingredients={turbofuel: (7.5 * 2.5)},
    output_per_minute=1,
    machine_type=MachineType.raw,
)

versatile_framework = Recipe(
    recipe_name="Versatile Framework",
    product_name="Versatile Framework",
    ingredients={modular_frame: 2.5, steel_beam: 30},
    output_per_minute=5,
    machine_type=MachineType.assembler,
)

flexible_framework = Recipe(
    recipe_name="Flexible Framework",
    product_name="Versatile Framework",
    ingredients={modular_frame: 3.75, steel_beam: 22.5, rubber: 30},
    output_per_minute=7.5,
    machine_type=MachineType.manufacturer,
)

encased_industrial_beam = Recipe(
    recipe_name="Encased Industrial Beam",
    product_name="Encased Industrial Beam",
    ingredients={steel_beam: 18, concrete: 36},
    output_per_minute=6,
    machine_type=MachineType.assembler,
)

encased_industrial_pipe = Recipe(
    recipe_name="Encased Industrial Pipe",
    product_name="Encased Industrial Beam",
    ingredients={steel_pipe: 24, concrete: 20},
    output_per_minute=4,
    machine_type=MachineType.assembler,
)

heavy_modular_frame = Recipe(
    recipe_name="Heavy Modular Frame",
    product_name="Heavy Modular Frame",
    ingredients={
        modular_frame: 10,
        steel_pipe: 40,
        encased_industrial_beam: 10,
        screw: 240,
    },
    output_per_minute=2,
    machine_type=MachineType.manufacturer,
)

heavy_encased_frame = Recipe(
    recipe_name="Heavy Encased Frame",
    product_name="Heavy Modular Frame",
    ingredients={
        modular_frame: 7.5,
        encased_industrial_beam: 9.375,
        steel_pipe: 33.75,
        concrete: 20.625,
    },
    output_per_minute=2.812,
    machine_type=MachineType.manufacturer,
)

heavy_flexible_frame = Recipe(
    recipe_name="Heavy Flexible Frame",
    product_name="Heavy Modular Frame",
    ingredients={
        modular_frame: 18.75,
        encased_industrial_beam: 11.25,
        rubber: 75,
        screw: 390,
    },
    output_per_minute=3.75,
    machine_type=MachineType.manufacturer,
)
