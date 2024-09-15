from models.recipes import *


def main():
    alts = {steel_ingot: solid_steel_ingot}
    # alts = {}
    res = steel_beam.calculate_requirements_for_rate(60, alts=alts, print_tree=True)
    print(res)


if __name__ == "__main__":
    main()
