

containers = [11,30,47,31,32,36,3,1,5,3,32,36,15,11,46,26,28,1,19,3]
containers.sort(reverse=True)
print(containers)

def get_combinations(containers:list[int], used_amount:int, total_amount:int, nr_of_possible_combinations:int) -> list[list[int]]:
    for i,container in enumerate(containers):
        if used_amount+container > total_amount:
            pass
        if used_amount+container == total_amount:
            nr_of_possible_combinations += 1
        elif used_amount+container < total_amount:
            used_amount = used_amount+container
            nr_of_possible_combinations = nr_of_possible_combinations + get_combinations(containers[i+1:-1], used_amount, total_amount, nr_of_possible_combinations)
    return nr_of_possible_combinations

print(get_combinations(containers, 0, 150, 0))


"""
Way smoother, but from the internet (https://www.reddit.com/r/adventofcode/comments/3x6cyr/comment/cy1xvqm/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
"""

import itertools

containers = [11,30,47,31,32,36,3,1,5,3,32,36,15,11,46,26,28,1,19,3]

combinations=[]
for i in range(1,len(containers)+1):
    for c in itertools.combinations(containers, i):
        if sum(c) == 150:
            combinations.append(c)
print(len(combinations))

minimum = min([len(combinations[i]) for i in range(len(combinations))])
print(minimum)
print(len([c for c in itertools.combinations(containers,minimum) if sum(c)==150]))
