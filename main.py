from models.recipes import *


def main():
    # alts2 = {fuel: diluted_packaged_fuel}
    # res = turbofuel_generator_250.calculate_requirements_for_rate(20, alts=alts2, print_tree=True)
    # print(res)

    alts = {steel_ingot: solid_steel_ingot}
    skipped = [modular_frame]
    res = versatile_framework.calculate_requirements_for_rate(
        20,
        alts=alts,
        print_tree=True,
        skipped_items=skipped
    )
    print(res)


if __name__ == "__main__":
    main()
