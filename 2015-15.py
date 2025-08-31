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

def get_input():
    data = pd.read_csv("2015-15.csv", index_col=0, encoding="utf-8")
    return data

def compute_optimization(data):
    a,b,c,d,e = 0,0,0,0,0
    score=0
    maximum=0
    for i in range(0,100):
        for j in range(0,100-i):
            for k in range(0,100-i-j):
                h = 100-i-j-k
                a=data[0][0]*i+data[1][0]*j+data[2][0]*k+data[3][0]*h
                if a<=0: continue
                b=data[0][1]*i+data[1][1]*j+data[2][1]*k+data[3][1]*h
                if b<=0: continue
                c=data[0][2]*i+data[1][2]*j+data[2][2]*k+data[3][2]*h
                if c<=0: continue
                d=data[0][3]*i+data[1][3]*j+data[2][3]*k+data[3][3]*h
                if d<=0: continue
                e=data[0][4]*i+data[1][4]*j+data[2][4]*k+data[3][4]*h
                
                if e!=500:
                    continue

                score = a*b*c*d
                maximum = max(score, maximum)

    return maximum

def main():
    data = get_input()
    data = [[2,0,-2,0,3],[0,5,-3,0,3],[0,0,5,-1,8],[0,-1,0,5,8]]
    print(compute_optimization(data))

main()