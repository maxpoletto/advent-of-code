#!/opt/local/bin/python

def part1(text):
    return text.count('(') - text.count(')')

def part2(text):
    f, p = 0, 0
    for c in text:
        p += 1
        if c == '(':
            f += 1
        elif c == ')':
            f -= 1
        if f == -1:
            return p
    return 0

fn = "input/input01.txt"
with open(fn) as f:
    lines = f.readlines()
    text = ''.join([ l.strip() for l in lines])

print(part1(text))
print(part2(text))
