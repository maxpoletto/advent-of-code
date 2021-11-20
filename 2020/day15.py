#!/usr/local/bin/python

def solve(nums, target):
    hist = {}
    for i in range(len(nums)-1):
        hist[nums[i]] = i+1 # turns are 1-indexed
    last, last_turn = nums[-1], len(nums)
    while last_turn < target:
        if last in hist:
            n = last_turn-hist[last]
        else:
            n = 0
        hist[last] = last_turn
        last_turn += 1
        last = n
    return last

print(solve([0,3,6], 2020))
print(solve([9,19,1,6,0,5,4], 2020))

print(solve([9,19,1,6,0,5,4], 30000000))
print(solve([0,3,6], 30000000))
print(solve([1,3,2], 30000000))
print(solve([2,1,3], 30000000))
print(solve([1,2,3], 30000000))
print(solve([2,3,1], 30000000))
print(solve([3,2,1], 30000000))
print(solve([3,1,2], 30000000))
