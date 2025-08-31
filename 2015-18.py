
import numpy as np

with open("2015-18.txt", "r") as f:
    grid = f.read().splitlines()

def valid_position(position:list[int]) -> bool:
    if position[0] < 0 or position[0] >= 100:
        return False
    if position[1] < 0 or position[1] >= 100:
        return False
    return True

def own_position(own_position:list[int], check_position:list[int]) -> bool:
    if own_position[0] == check_position[0]:
        if own_position[1] == check_position[1]:
            return True
    return False

def get_neighbour_lights_on(position:list[int,int], grid:list[str]) -> int:
    count = 0
    for x in range(position[0]-1, position[0]+2):
        for y in range(position[1]-1, position[1]+2):
            if valid_position([x,y]) and grid[x][y] == '#' and not own_position(position, [x,y]):
                count+=1
    return count


for i in range(100):
    new_grid = []
    for x in range(100):
        line=""
        for y in range(100):
            if (x==0 or  x==99) and (y==0 or y==99):
                line = line + "#"
            elif grid[x][y] == '#' and (get_neighbour_lights_on([x,y],grid)==2 or get_neighbour_lights_on([x,y],grid)==3):
                line = line + '#'
            elif grid[x][y] == '.' and get_neighbour_lights_on([x,y],grid)==3:
                line = line + '#'
            else: line = line + '.'
        new_grid.append(line)
    grid = new_grid
    print(i)

print(grid[0])

count = 0
for line in grid:
    count += line.count("#")

print(count)