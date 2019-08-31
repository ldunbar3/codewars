# https://www.codewars.com/kata/pete-the-baker/train/python

'''
Write a function cakes(), which takes the recipe (object) and the available ingredients 
(also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity 
there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
Ingredients that are not present in the objects, can be considered as 0.
'''

def cakes(recipe, available):
    for ingredient in recipe:
        if ingredient not in available:
            return 0
            
    d = {}
    for ingredient in available:
        if ingredient in recipe:
            d[ingredient] = available.get(ingredient)
    available = d
    recipe = dict(sorted(recipe.iteritems()))
    available = dict(sorted(available.iteritems()))
    return min(ingredient[1] / ingredient[0] for ingredient in zip(recipe.values(), available.values()))