#!/opt/local/bin/python

def part1(boxes):
    t = 0
    for b in boxes:
        t += 2*(b[0]*b[1] + b[1]*b[2] + b[0]*b[2])+b[0]*b[1]
    return t

def part2(boxes):
    t = 0
    for b in boxes:
        t += b[0]*b[1]*b[2] + 2*b[0] + 2*b[1]
    return t

fn = "input/input02.txt"
boxes = []
with open(fn) as f:
    for l in f:
        l = l.strip()
        boxes.append(sorted([int(x) for x in l.split('x')]))

print(part1(boxes))
print(part2(boxes))
