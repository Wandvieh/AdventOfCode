"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

    123 -> x means that the signal 123 is provided to wire x.
    x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
"""

import re
import pandas as pd

def getNumber(a, wires):
    if type(a) == int:
        return a
    else: return wires["a"]

def goThroughLines(input):
    for line in input:
        temp, wire = re.split(" -> ", line)
        action = re.split(" ", temp)

        # Check if this is already implemented
        if wire in wires.keys(): continue

        # Case: action has length 1. Check if I can work on this line
        elif len(action) == 1:
            """if wire == 'b': #only enable for Part 2
                wires[wire] = 956
                continue"""
            try:
                number = int(action[0])
                wires[wire] = number
            except:
                if action[0] in wires.keys():
                    wires[wire] = wires[action[0]]
                else: continue # can't work on this
        # Case: action has length 2. Check if I can work on this line
        elif len(action) == 2:
            try:
                number = int(action[1])
                wires[wire] = ~number
            except:
                if action[1] in wires.keys():
                    wires[wire] = ~wires[action[1]]
                else: continue # can't work on this
        # Case: action has length 3. first check for lshift/rshift, then and, then or
        elif action[1] == 'RSHIFT' or action[1] == 'LSHIFT':
            if action[0] not in wires.keys(): continue # can't work on this (lshift/rshift)
            if action[1] == 'RSHIFT':
                wires[wire] = wires[action[0]] >> int(action[2])
            if action[1] == 'LSHIFT':
                wires[wire] = wires[action[0]] << int(action[2])
        elif action[1] == 'AND':
            if action[2] not in wires.keys(): continue # can't work on this (AND, second variable)
            try:
                number = int(action[0])
                wires[wire] = number & wires[action[2]]
            except:
                if action[0] in wires.keys():
                    wires[wire] = wires[action[0]] & wires[action[2]]
                else: continue # can't work on this (AND, first variable)
        else:
            if action[2] not in wires.keys(): continue # can't work on this (OR, second variable)
            try:
                number = int(action[0])
                wires[wire] = number | wires[action[2]]
            except:
                if action[0] in wires.keys():
                    wires[wire] = wires[action[0]] | wires[action[2]]
                else: continue # can't work on this (OR, first variable)
    return

with open('2015-07.txt', 'r') as f:  
    input = f.read().split('\n')

wires = {}

while True:
    goThroughLines(input)
    if 'a' in wires.keys(): break

print(wires['a']) #956, part 2 is 40149

"""
--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
"""
