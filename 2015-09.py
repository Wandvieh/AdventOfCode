"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141

The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?
"""

import pandas as pd
import numpy as np
import re
import timeit
start = timeit.default_timer()

cities = ["AlphaCentauri", "Snowdin", "Tambi", "Faerun", "Norrath", "Straylight", "Tristram", "Arbre"]
with open('2015-09.txt', 'r') as f:  
    input = f.read().split('\n')
data = pd.DataFrame(index=cities, columns=cities)

for line in input:
    data[re.findall("([A-Za-z]+) to ", line)[0]][re.findall(" to ([A-Za-z]+)", line)[0]] = int(re.findall("[0-9]+", line)[0])
    data[re.findall(" to ([A-Za-z]+)", line)[0]][re.findall("([A-Za-z]+) to ", line)[0]] = int(re.findall("[0-9]+", line)[0])
print(data)

visited_cities_shortest = ['', '', '', '', '', '', '', '']
shortest_distance = np.inf
longest_distance = 0
visited_cities_longest = ['', '', '', '', '', '', '', '']

data.info()
"""
print(data["AlphaCentauri"]["Snowdin"] + data["Snowdin"]["Tambi"])
print(data["AlphaCentauri"]["Snowdin"], data["Snowdin"]["Tambi"])
exit()"""

for i1 in cities:
    for i2 in cities:
        if i1 == i2: continue
        for i3 in cities:
            if i1 == i3 or i2 == i3: continue
            for i4 in cities:
                if i1 == i4 or i2 == i4 or i3 == i4: continue
                for i5 in cities:
                    if i1 == i5 or i2 == i5 or i3 == i5 or i4 == i5: continue
                    for i6 in cities:
                        if i1 == i6 or i2 == i6 or i3 == i6 or i4 == i6 or i5 == i6: continue
                        for i7 in cities:
                            if i1 == i7 or i2 == i7 or i3 == i7 or i4 == i7 or i5 == i7 or i6 == i7: continue
                            for i8 in cities:
                                if i1 == i8 or i2 == i8 or i3 == i8 or i4 == i8 or i5 == i8 or i6 == i8 or i7 == i8: continue
                                distance = (data[i1][i2] + data[i2][i3] + data[i3][i4]+ data[i4][i5]+ data[i5][i6]+ data[i6][i7]+ data[i7][i8])
                                print("Iteration Done")
                                if distance < shortest_distance:
                                    shortest_distance = distance
                                    visited_cities_shortest = [i1, i2, i3, i4, i5, i6, i7, i8]
                                    print(visited_cities_shortest)
                                    print("Distance:", distance)
                                if distance > longest_distance:
                                    longest_distance = distance
                                    visited_cities_longest = [i1, i2, i3, i4, i5, i6, i7, i8]
                                    print(visited_cities_longest)
                                    print("Distance:", distance)
print(shortest_distance) # 141
print(visited_cities_shortest) # ['Tristram', 'AlphaCentauri', 'Norrath', 'Straylight', 'Faerun', 'Snowdin', 'Tambi', 'Arbre']
print(longest_distance) # 736
print(visited_cities_longest) # ['AlphaCentauri', 'Arbre', 'Tristram', 'Snowdin', 'Straylight', 'Tambi', 'Norrath', 'Faerun']

stop = timeit.default_timer()
print('Time: ', stop - start) # 3.7315396999474615

"""
--- Part Two ---

The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?
"""