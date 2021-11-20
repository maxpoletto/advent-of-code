#!/usr/local/bin/python

from lib import aodfile
import re

def part1(lines):
    nice = 0
    for l in lines:
        if re.match(r'.*(?:ab|cd|pq|xy)', l):
            continue
        if not re.match(r'.*([a-z])\1', l):
            continue
        if not re.match(r'(.*[aeiou]){3,}', l):
            continue
        nice += 1
    return nice

def part2(lines):
    nice = 0
    for l in lines:
        if not re.match(r'.*([a-z][a-z]).*\1', l):
            continue
        if not re.match(r'.*([a-z])[a-z]\1', l):
            continue
        nice += 1
    return nice

fn = "input/input05.txt"
lines = aodfile.stripped_lines(fn)
print(part1(lines))
print(part2(lines))
