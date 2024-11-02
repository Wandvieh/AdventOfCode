"""
Trying so solve Day 9 differently
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
#print(data)

visited_cities_shortest = ['', '', '', '', '', '', '', '']
shortest_distance = np.inf
longest_distance = 0
visited_cities_longest = ['', '', '', '', '', '', '', '']

data.info()
"""
print(data["AlphaCentauri"]["Snowdin"] + data["Snowdin"]["Tambi"])
print(data["AlphaCentauri"]["Snowdin"], data["Snowdin"]["Tambi"])
exit()"""

for i2 in cities[1:]:
    for i3 in cities[1:]:
        if i2 == i3: continue
        for i4 in cities[1:]:
            if i2 == i4 or i3 == i4: continue
            for i5 in cities[1:]:
                if i2 == i5 or i3 == i5 or i4 == i5: continue
                for i6 in cities[1:]:
                    if i2 == i6 or i3 == i6 or i4 == i6 or i5 == i6: continue
                    for i7 in cities[1:]:
                        if i2 == i7 or i3 == i7 or i4 == i7 or i5 == i7 or i6 == i7: continue
                        for i8 in cities[1:]:
                            if i2 == i8 or i3 == i8 or i4 == i8 or i5 == i8 or i6 == i8 or i7 == i8: continue
                            helper = [data["AlphaCentauri"][i2], data[i2][i3], data[i3][i4], data[i4][i5], data[i5][i6], data[i6][i7], data[i7][i8], data[i8]["AlphaCentauri"]]
                            #out = max(helper)
                            distance1 = (sum(helper) - max(helper))
                            distance2 = (sum(helper) - min(helper))
                            #print("Iteration Done")
                            if distance1 < shortest_distance:
                                shortest_distance = distance1
                                visited_cities_shortest = ["AlphaCentauri", i2, i3, i4, i5, i6, i7, i8]
                                print(visited_cities_shortest, helper)
                                print("Distance:", distance1)
                            if distance2 > longest_distance:
                                longest_distance = distance2
                                visited_cities_longest = ["AlphaCentauri", i2, i3, i4, i5, i6, i7, i8]
                                print(visited_cities_longest, helper)
                                print("Distance:", distance2)

print(shortest_distance) # 141
print(visited_cities_shortest) # ['Tristram', 'AlphaCentauri', 'Norrath', 'Straylight', 'Faerun', 'Snowdin', 'Tambi', 'Arbre']
print(longest_distance) # 736
print(visited_cities_longest) # ['AlphaCentauri', 'Arbre', 'Tristram', 'Snowdin', 'Straylight', 'Tambi', 'Norrath', 'Faerun']

stop = timeit.default_timer()
print('Time: ', stop - start) # 0.14856589992996305

# It worked for the shortest distance
# After making a difference between distance1 and distance2, the longest distance also worked
# I just can't see the visited cities anymore
# And it's a lot faster than the previous version