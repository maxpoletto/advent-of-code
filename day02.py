#!/opt/local/bin/python

import re

def part1(rules):
    n_valid = 0
    for r in rules:
        n = r[-1].count(r[-2])
        if n >= r[0] and n <= r[1]:
            n_valid += 1
    return n_valid

def part2(rules):
    n_valid = 0
    for r in rules:
        if (r[-2] == r[-1][r[0]-1]) != (r[-2] == r[-1][r[1]-1]):
            n_valid += 1
    return n_valid

filename = "input02.txt"
regex = re.compile(r'(\d+)-(\d+)\s+(\w):\s+(\w+)')
rules = []
with open(filename) as file:
    for line in file:
        m = regex.fullmatch(line.strip())
        if m is None:
            continue
        rules.append([int(m[1]), int(m[2]), m[3], m[4]])

print(part1(rules))
print(part2(rules))
