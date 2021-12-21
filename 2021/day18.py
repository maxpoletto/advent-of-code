from copy import deepcopy
from lib import aodfile

def magnitude(num):
    if isinstance(num, int):
        return num
    return 3*magnitude(num[0]) + 2*magnitude(num[1])

def do_explode(num, n, state, depth):
    if isinstance(num[n], list):
        if "nextright" in state.keys():
            return exploder(num[n], state, depth+1)
        elif depth == 3:
            if "prevleft" in state.keys():
                num2, i = state["prevleft"]
                num2[i] += num[n][0]
            state["nextright"] = num[n][1]
            num[n] = 0
        else:
            return exploder(num[n], state, depth+1)
    else:
        if "nextright" in state.keys():
            num[n] += state["nextright"]
            return True
        else:
            state["prevleft"] = (num, n)
    return False

def exploder(num, state, depth):
    assert(isinstance(num, list))
    return (do_explode(num, 0, state, depth)
            or do_explode(num, 1, state, depth)
            or (depth == 0 and "nextright" in state.keys()))

def explode(num):
    state = {}
    return exploder(num, state, 0)

def do_split(num, n, depth):
    if isinstance(num[n], int):
        if num[n] > 9:
            num[n] = [int(num[n]/2), int((1+num[n])/2)]
            return True
        return False
    return splitr(num[n], depth+1)

def splitr(num, depth):
    return do_split(num, 0, depth) or do_split(num, 1, depth)

def split(num):
    assert(isinstance(num, list))
    return splitr(num, 0)

def reduce(num):
    while explode(num) or split(num):
        pass
    return num

def sum(n1, n2):
    n1, n2 = deepcopy(n1), deepcopy(n2)
    return reduce([n1, n2])

def part1():
    n = nums[0]
    for n2 in nums[1:]:
        n = sum(n, n2)
    print(magnitude(n))

def part2():
    big = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            big = max(big, magnitude(sum(nums[i], nums[j])), magnitude(sum(nums[j], nums[i])))
    print(big)

nums = []
for l in aodfile.stripped_lines("input/input18.txt"):
    nums.append(eval(l))
part1()
part2()
