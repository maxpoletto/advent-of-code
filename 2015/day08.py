#!/opt/local/bin/python

from lib import aodfile
import re

def part1(lines):
    a,b = 0,0
    for l in lines:
        a += len(l)
        l = re.sub(r'\\\\', r'#', l)
        l = re.sub(r'\\"', r'"', l)
        l = re.sub(r'\\x[0-9a-f][0-9a-f]', r'.', l)
        b += len(l)-2 # 2 for the outer quotes
    return a-b

def part2(lines):
    a,b = 0,0
    for l in lines:
        a += len(l)
        l = re.sub(r'\\', r'\\\\', l)
        l = re.sub(r'"', r'\\"', l)
        b += len(l)+2 # 2 for the outer quotes
    return b-a

fn = "input/input08.txt"
lines = aodfile.stripped_lines(fn)
print(part1(lines))
print(part2(lines))
