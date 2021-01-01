import re
import sys
from collections import defaultdict

def parseFood(line):
    line = line.strip().replace(")", "")
    tokens = line.split("(contains ")
    (lhs, rhs) = tokens
    lhs = lhs.strip()
    ingredients = set(lhs.split())
    allergens = set(rhs.split(", "))
    return (ingredients, allergens)

FOODS = []
INGREDIENTS = set()
ALLERGENS = set()
ALLERGEN_INGS = {}

def main():
    with open(sys.argv[1]) as fh:
        for line in fh:
            food = parseFood(line)
            for ing in food[0]:
                INGREDIENTS.add(ing)
            FOODS.append(food)

    foodsByAllergen = defaultdict(lambda: [])
    for (ingredients, allergens) in FOODS:
        for allergen in allergens:
            ALLERGENS.add(allergen)
            foodsByAllergen[allergen].append((ingredients, allergens))
    allergenIngredientCandidates = {}
    for (allergen, foods) in foodsByAllergen.items():
        candidates = INGREDIENTS
        for food in foods:
            candidates = candidates & food[0]
        allergenIngredientCandidates[allergen] = candidates
    allergenIngredients = {}
    while len(allergenIngredientCandidates) > 0:
        foundAllergen = None
        for (allergen, ingredients) in allergenIngredientCandidates.items():
            if len(ingredients) == 1:
                foundAllergen = allergen
                break
        if foundAllergen != None:
            foundIngredient = next(iter(ingredients))
            allergenIngredients[foundAllergen] = foundIngredient
            del allergenIngredientCandidates[foundAllergen]
            for (allergen, candidates) in allergenIngredientCandidates.items():
                candidates.discard(foundIngredient)
    badIngredients = set([v for v in allergenIngredients.values()])
    counter = 0
    for (ings, alls) in FOODS:
        for ing in ings:
            if not (ing in badIngredients):
                counter += 1
    print(counter)
    allergenTable = list(allergenIngredients.items())
    allergenTable.sort()
    print(",".join(v for (a, v) in allergenTable))

main()

