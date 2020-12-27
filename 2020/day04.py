#!/opt/local/bin/python

import re

def is_valid1(info):
    return len(info) == 8 or (len(info) == 7 and "cid" not in info)

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

def is_valid2(info):
    if len(info) != 8 and not (len(info) == 7 and "cid" not in info):
        return False
    if not valid_num(info["byr"], 4, 1920, 2002):
        return False
    if not valid_num(info["iyr"], 4, 2010, 2020):
        return False
    if not valid_num(info["eyr"], 4, 2020, 2030):
        return False
    if not valid_height(info["hgt"]):
        return False
    if not re.fullmatch(r'#[0-9a-f]{6}', info["hcl"]):
        return False
    if not info["ecl"] in valid_color:
        return False
    if not valid_num(info["pid"], 9, 0, 999999999):
        return False
    return True

def part1(passports):
    return sum([is_valid1(p) for p in passports])

def part2(passports):
    return sum([is_valid2(p) for p in passports])

regex = re.compile(r'(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):([^\s]+)')
passports, info = [], {}
fn = "input04.txt"
with open(fn) as f:
    for l in f:
        l = l.strip()
        if len(l) == 0:
            passports.append(info)
            info = {}
        else:
            for i in regex.findall(l):
                info[i[0]] = i[1]
if len(info) > 0:
    passports.append(info)

print(part1(passports))
print(part2(passports))
