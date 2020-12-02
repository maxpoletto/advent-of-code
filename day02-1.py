#!/opt/local/bin/python

import re

filename = "input02.txt"
regex = re.compile(r'(\d+)-(\d+)\s+(\w):\s+(\w+)')

n_valid = 0
n_total = 0
with open(filename) as file:
    for line in file:
        m = regex.fullmatch(line.strip())
        if m is None:
            continue
        n_total += 1
        n, lo, hi, char, password = 0, int(m[1]), int(m[2]), m[3], m[4]
        for c in password:
            if c == char:
                n += 1
        if n >= lo and n <= hi:
            n_valid += 1

print(n_valid, "valid passwords out of", n_total, "total")
