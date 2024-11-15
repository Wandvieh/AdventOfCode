"""
--- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

    [1,2,3] and {"a":2,"b":4} both have a sum of 6.
    [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
    {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
    [] and {} both have a sum of 0.

You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?
"""

"""import re

f = open("2015-12.json", "r")
input = f.read()

numbers = [int(item) for item in re.findall("-*[0-9]+", input)]
print(numbers)
print(sum(numbers)) # 156366"""


"""
--- Part Two ---

Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

    [1,2,3] still has a sum of 6.
    [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
    {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
    [1,"red",5] has a sum of 6, because "red" in an array has no effect.
"""

"""red_objects = re.findall('\{[0-9a-z,:\s"-\[\]]*red[0-9a-z,:\s"-\[\]]*\}', input)
print(red_objects)
print(len(red_objects))

for i in red_objects:
    for j in red_objects:
        if i in j:
            red_objects.remove(i)
print(red_objects)
print(len(red_objects))

red_objects_numbers = []
for object in red_objects:
    red_objects_numbers.extend([int(item) for item in re.findall("-*[0-9]+", object)])
#print(red_objects_numbers)
print(sum(numbers) - sum(red_objects_numbers))"""

import json
import re

def check_json(json, reds):
    for entry in json:
        if type(entry) is dict:
            print(entry)
            print("1", reds)
            for key, value in entry.items():
                check = False
                if value == "red":
                    #print(key)
                    reds.append(entry)
                    #print(reds)
                    check = True
                    print("2", reds)
                    break
            print("3", reds)
            if check: continue
            print("4", reds)
            for key, value in entry.items():
                if type(value) is dict or type(value) is list:
                    check_json(value, reds)
            print("5", reds)
        if (type(entry)) is list:
            for item in entry:
                if type(item) is dict or type(item) is list:
                    check_json(item, reds)
    
    print("6", reds)
    return reds

test = [ {
    "a": {"b": "red", "c": [1, 2], "d": 3},
    "e": [4, 5, 6],
    "f": {"g": "blue", "h": 7, "i": [8, "j", 9]}
} ]

f = open("2015-12.txt", "r")
x = json.loads(f.read())
reds = []

reds = check_json(test, reds)

input2 = json.dumps(reds)

numbers2 = [int(item) for item in re.findall("-*[0-9]+", input2)]

#print(sum(numbers)-sum(numbers2))
print(numbers2)
print(sum(numbers2))
