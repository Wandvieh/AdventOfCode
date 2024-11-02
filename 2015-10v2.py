"""
Trying solutions from the subreddit
"""

"""import re
re_d = re.compile(r'((\d)\2*)')
print(re_d)

def replace(match_obj):
    s = match_obj.group(1)
    return str(len(s)) + s[0]

s = '1321131112'
for i in range(2):
    s = re_d.sub(replace,s)
    print(s)

print(len(s))"""

from itertools import groupby

def look_and_say(input_string, num_iterations):
    for i in range(num_iterations):
        input_string = ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])
        print(i)
    return input_string

print(len(look_and_say('1113122113', 50))) # 5103798