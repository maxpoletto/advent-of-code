#!/opt/local/bin/python

import re

filename = "input04.txt"

def is_valid(info):
    if len(info) == 8 or (len(info) == 7 and "cid" not in info):
        print("valid", len(info), sorted(info.keys()))
        return 1
    print("invalid", len(info), sorted(info.keys()))
    return 0

nvalid, ntotal = 0, 0
regex = re.compile(r'(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):([^\s]+)')
info = {}
with open(filename) as f:
    for l in f:
        l = l.strip()
        if len(l) == 0:
            nvalid += is_valid(info)
            ntotal += 1
            info = {}
        else:
            for i in regex.findall(l):
                info[i[0]] = i[1]
if len(info) > 0:
    nvalid += is_valid(info)
    ntotal += 1
print(nvalid, "valid passports out of", ntotal)
