class Recipe:
    def __init__(self, name:str=None, output_per_minute:int=None, ingredients:list=None):
        self.name = name
        self.output_per_minute = output_per_minute
        self.ingredients = ingredients

class Item:
    def __init__(self, name:str=None, recipes:list=None):
        self.name = name
        self.recipes = recipes if recipes is not None else list()
