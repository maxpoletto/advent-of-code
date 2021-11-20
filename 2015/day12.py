#!/usr/local/bin/python

from lib import aodfile
import re

def count(o):
    if type(o) == int:
        return o
    t = 0
    if type(o) == list:
        for k in o:
            t += count(k)
    elif type(o) == dict:
        for k in o:
            if o[k] == 'red':
                return 0
        for k in o:
            t += count(o[k])
    return t            

def part1(txt):
    return sum([int(x) for x in re.findall(r'\-?\d+', txt)])

def part2(txt):
    return count(eval(txt))

fn = "input/input12.txt"
txt = aodfile.stripped_text(fn)
print(part1(txt))
print(part2(txt))
