"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

    capacity (how well it helps the cookie absorb milk)
    durability (how well it keeps the cookie intact when full of milk)
    flavor (how tasty it makes the cookie)
    texture (how it improves the feel of the cookie)
    calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

    A capacity of 44*-1 + 56*2 = 68
    A durability of 44*-2 + 56*3 = 80
    A flavor of 44*6 + 56*-2 = 152
    A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
"""

import re
import pprint
import pandas as pd

data = {}
with open('2015-15.txt', 'r') as f:  
    input = f.read().split('\n')
for line in input:
    name = re.findall("^[A-Za-z]+", line)[0]
    data[name] = {}
    data[name]["capacity"] = int(re.findall("capacity (-*[0-9]+)", line)[0])
    data[name]["durability"] = int(re.findall("durability (-*[0-9]+)", line)[0])
    data[name]["flavor"] = int(re.findall("flavor (-*[0-9]+)", line)[0])
    data[name]["texture"] = int(re.findall("texture (-*[0-9]+)", line)[0])
    data[name]["calories"] = int(re.findall("calories (-*[0-9]+)", line)[0])
#pprint.pprint(data)

df = pd.DataFrame(data)
print(df)

# First get all combinations (List of Dictionaries)
# Optional: Skip something when it produces a negative (zero) outcome
def get_all_combinations(ingredients, allCombinations, currCombination, depth, counter):
    for i in range(1, counter+1):
        if depth == 1:
            currCombination = []
        if i == counter:
            allCombinations.append([counter, 0, 0, 0])
            return allCombinations, currCombination
        if len(ingredients) == 1:
            currCombination.append(4 - sum(currCombination))
            #print(currCombination)
            allCombinations.append(currCombination)
            currCombination = currCombination[:-2]
        else:
            currCombination.append(i)
            remainingIngredients = ingredients.copy()
            remainingIngredients.remove(ingredients[0])
            allCombinations, currCombination = get_all_combinations(remainingIngredients, allCombinations, currCombination, depth+1, counter)
        #if depth == 1:
        #    print(i)
    

# Then go through all dictionaries to find best solution

counter = 5
allCombinations, currCombination = get_all_combinations(["Sprinkles","Butterscotch","Chocolate","Candy"], [], [], 1, counter)
#print(allCombinations)