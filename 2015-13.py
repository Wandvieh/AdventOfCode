"""--- Day 13: Knights of the Dinner Table ---

In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.

Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83

After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?
"""

import pandas as pd
import re

seats = [1, 2, 3, 4, 5, 6, 7, 8]
participants = ["Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory"]
with open('2015-13.txt', 'r') as f:  
    input = f.read().split('\n')
data = pd.DataFrame(index=participants, columns=participants)
#print(data)

for line in input:
    if "gain" in line:
        data[re.findall("^[A-Za-z]+", line)[0]][re.findall("([A-Za-z]+)\.", line)[0]] = int(re.findall("[0-9]+", line)[0])
    if "lose" in line:
        data[re.findall("^[A-Za-z]+", line)[0]][re.findall("([A-Za-z]+)\.", line)[0]] = -int(re.findall("[0-9]+", line)[0])
print(data)

def calculate_happiness(seating, data):
    happiness = 0
    for i in range(len(seating)):
        happiness += data[seating[i]][seating[(i-1)%8]]
        happiness += data[seating[i]][seating[(i+1)%8]]
    print(happiness)
    return happiness

optimal_seating = participants
optimal_happiness = calculate_happiness(optimal_seating, data)
curr_seating = []
curr_happiness = 0

for i1 in participants:
    for i2 in participants:
        if i1 == i2: continue
        for i3 in participants:
            if i1 == i3 or i2 == i3: continue
            for i4 in participants:
                if i1 == i4 or i2 == i4 or i3 == i4: continue
                for i5 in participants:
                    if i1 == i5 or i2 == i5 or i3 == i5 or i4 == i5: continue
                    for i6 in participants:
                        if i1 == i6 or i2 == i6 or i3 == i6 or i4 == i6 or i5 == i6: continue
                        for i7 in participants:
                            if i1 == i7 or i2 == i7 or i3 == i7 or i4 == i7 or i5 == i7 or i6 == i7: continue
                            for i8 in participants:
                                if i1 == i8 or i2 == i8 or i3 == i8 or i4 == i8 or i5 == i8 or i6 == i8 or i7 == i8: continue
                                curr_seating = [i1, i2, i3, i4, i5, i6, i7, i8]
                                curr_happiness = calculate_happiness(curr_seating, data)
                                if curr_happiness > optimal_happiness:
                                    optimal_seating = curr_seating
                                    optimal_happiness = curr_happiness
                                    print(optimal_happiness, optimal_seating)

print(optimal_happiness) # 618
print(optimal_seating) # ['Alice', 'Eric', 'Bob', 'Carol', 'David', 'George', 'Mallory', 'Frank']

"""
--- Part Two ---

In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?
"""

import numpy as np

best_change = np.inf
for i in range(len(optimal_seating)):
    curr_change = 0
    curr_change += data[optimal_seating[i]][optimal_seating[(i-1)%8]]
    curr_change += data[optimal_seating[(i-1)%8]][optimal_seating[i]]
    print(curr_change)
    if curr_change < best_change:
        best_change = curr_change
print(best_change)

print(optimal_happiness - best_change) # 601