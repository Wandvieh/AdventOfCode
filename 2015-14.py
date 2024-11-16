"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

    Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?
"""

import re
import pprint

data = {}
with open('2015-14.txt', 'r') as f:  
    input = f.read().split('\n')
for line in input:
    name = re.findall("^[A-Za-z]+", line)[0]
    data[name] = {}
    data[name]["speed"] = int(re.findall("([0-9]+)\skm", line)[0])
    data[name]["flytime"] = int(re.findall("([0-9]+) seconds,", line)[0])
    data[name]["resttime"] = int(re.findall("([0-9]+) seconds\.", line)[0])
pprint.pprint(data)

def check_distance(specifics, time):
    nr_cycles = int(time / (specifics["flytime"] + specifics["resttime"]))
    distance = nr_cycles * specifics["flytime"] * specifics["speed"]
    print(nr_cycles)
    print(distance)

    rest = time % (specifics["flytime"] + specifics["resttime"])
    print(rest)
    if specifics["flytime"] > rest:
        distance += rest * specifics["speed"]
        print(distance)
        return distance
    else:
        distance += specifics["flytime"] * specifics["speed"]
        print(distance)
        return distance

best_distance = 0
best_reindeer = ""
time = 2503

for reindeer, specifics in data.items():
    #print("Reindeer:", reindeer)
    distance = check_distance(specifics, time)
    if best_distance < distance:
        best_distance = distance
        best_reindeer = reindeer

print(best_reindeer, best_distance) # Cupid, 2696

"""
--- Part Two ---

Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?
"""

time = 2503

data2 = {}
for reindeer, specifics in data.items():
    data2[reindeer] = {}
    data2[reindeer]["distance"] = 0
    data2[reindeer]["points"] = 0
    data2[reindeer]["pointers"] = [True] * specifics["flytime"] + [False] * specifics["resttime"]

#furthest_distance = 0

for i in range (1, time+1):
    print("Round", i)
    furthest_distance = 0
    furthest_reindeer = ""
    for reindeer, specifics in data2.items():
        if specifics["pointers"][(i-1) % len(specifics["pointers"])]:
            specifics["distance"] += data[reindeer]["speed"]
        if specifics["distance"] > furthest_distance:
            furthest_distance = specifics["distance"]
            furthest_reindeer = reindeer
    for reindeer, specifics in data2.items():
        if specifics["distance"] == furthest_distance:
            specifics["points"] += 1
        print(reindeer, specifics["distance"], specifics["points"])

# Rudolph, 1084 points