import re

def part1():
    m = []
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    with open("input/i03.txt") as f:
        sumprod = 0
        for l in f:
            # Match all instances of pattern and extract values
            for m in pattern.finditer(l):
                sumprod += int(m.group(1)) * int(m.group(2))
        print(sumprod)

def part2():
    m = []
    pattern = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)")
    with open("input/i03.txt") as f:
        sumprod = 0
        x = 1
        for l in f:
            # Match all instances of pattern and extract values
            for m in pattern.finditer(l):
                if m.group(0) == "do()":
                    x = 1
                elif m.group(0) == "don't()":
                    x = 0
                else:
                    sumprod += x * int(m.group(1)) * int(m.group(2))
        print(sumprod)

part1()
part2()
