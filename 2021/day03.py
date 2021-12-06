import re
from collections import defaultdict
from collections import deque
from itertools import permutations
from lib import aodfile

def bitcnt(nums, cond):
    res, num_digits = 0, len(nums[0])
    for d in range(num_digits):
        s = ''.join(n[d] for n in nums)
        res *= 2
        res += cond(s)
    return res

def bitcnt2(nums, cond):
    num_digits = len(nums[0])
    for d in range(num_digits):
        s = ''.join(n[d] for n in nums)
        f = '01'[cond(s)]
        if len(nums) == 1:
            return int(nums[0], base=2)
        nums2 = []
        for n in nums:
            if n[d] == f:
                nums2.append(n)
        nums = nums2
    return int(nums[0], base=2)

def part1():
    nums = aodfile.stripped_lines("input/input03.txt")
    g = bitcnt(nums, lambda x: x.count('1') > x.count('0'))
    e = bitcnt(nums, lambda x: x.count('1') < x.count('0'))
    print(g*e)

def part2():
    nums = aodfile.stripped_lines("input/input03.txt")
    o = bitcnt2(nums, lambda x: x.count('1') >= x.count('0'))
    c = bitcnt2(nums, lambda x: x.count('1') < x.count('0'))
    print(o*c)

part1()
part2()
