#!/opt/local/bin/python

import re

filename = "input04.txt"

def valid_num(s, l, min, max):
    if (len(s)) != l:
        return False
    if not re.fullmatch(r'\d+', s):
        return False
    i = int(s)
    return i >= min and i <= max

def valid_height(s):
    m = re.fullmatch(r'(\d+)(cm|in)', s)
    if m is None:
        return False
    h = int(m[1])
    return (m[2] == "cm" and h >= 150 and h <= 193) or (m[2] == "in" and h >= 59 and h <= 76)

valid_color = { "amb":True, "blu":True, "brn":True, "gry":True, "grn":True, "hzl":True, "oth":True }

def is_valid(info):
    if len(info) != 8 and not (len(info) == 7 and "cid" not in info):
        return 0
    if not valid_num(info["byr"], 4, 1920, 2002):
        return 0
    if not valid_num(info["iyr"], 4, 2010, 2020):
        return 0
    if not valid_num(info["eyr"], 4, 2020, 2030):
        return 0
    if not valid_height(info["hgt"]):
        return 0
    if not re.fullmatch(r'#[0-9a-f]{6}', info["hcl"]):
        return 0
    if not info["ecl"] in valid_color:
        return 0
    if not valid_num(info["pid"], 9, 0, 999999999):
        return 0
    return 1

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
