from models import recipes


def main():
    res = recipes.iron_alloy_ingot.calculate_requirements_for_rate(50, print_tree=True)
    print(res)


if __name__ == "__main__":
    main()
