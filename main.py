from models.recipes import *


def main():
    # alts2 = {fuel: diluted_packaged_fuel}
    # res = turbofuel_generator_250.calculate_requirements_for_rate(20, alts=alts2, print_tree=True)
    # print(res)

    # alts = {}
    # skipped = []
    # res, power = iron_rod.calculate_requirements_for_rate(
    #     60, alts=alts, skipped_items=skipped, print_tree=True
    # )
    # print(res, power)

    alts = {
        heavy_modular_frame: heavy_encased_frame,
        steel_ingot: solid_steel_ingot,
        encased_industrial_beam: encased_industrial_pipe,
        concrete: wet_concrete,
        reinforced_iron_plate: stitched_iron_plate,
        # wire: iron_wire
    }
    skipped = []
    res, power = heavy_modular_frame.calculate_requirements_for_rate(
        5, alts=alts, print_tree=True, skipped_items=skipped
    )
    print(res, power)


if __name__ == "__main__":
    main()
