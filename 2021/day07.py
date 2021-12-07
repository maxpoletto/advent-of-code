import sys
from typing import Callable
from lib import aodfile

def min_fuel(burn: Callable[[int, int], int]) -> int:
    pos = list(map(int, aodfile.comma_separated("input/input07.txt")))
    fuel = sys.maxsize
    for i in range(min(pos), max(pos)+1):
        t = 0
        for p in pos:
            t += burn(p, i)
        if t < fuel:
            fuel = t
    return fuel

def part1():
    print(min_fuel(lambda x, y: abs(x-y)))

def part2():
    def burn(x, y):
        t = abs(x-y)
        return int(t*(t+1)/2)
    print(min_fuel(burn))

part1()
part2()
