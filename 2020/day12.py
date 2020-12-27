#!/opt/local/bin/python

import re

headings = [ 'E', 'S', 'W', 'N' ]
moves = {
    'N': ( 0, 1),
    'S': ( 0,-1),
    'E': ( 1, 0),
    'W': (-1, 0)
}
def new_heading(h, r):
    """Returns new heading given heading h and CW rotation r degrees."""
    for i in range(len(headings)):
        if headings[i] == h:
            return headings[(i + int(r/90)) % len(headings)]

def new_pos(p, h, d):
    """Returns new position given position p, heading h, distance d."""
    return [p[0] + d*moves[h][0], p[1] + d*moves[h][1]]

def new_wp(wp, d):
    """Returns new waypoint given by rotating waypoint wp by d degrees."""
    r = int(d/90)%4
    if r == 1: return [wp[1], -wp[0]]
    elif r == 2: return [-wp[0], -wp[1]]
    elif r == 3: return [-wp[1], wp[0]]
    return wp

def new_pos_wp(p, wp, d):
    """Returns position obtained by moving d times towards waypoint wp from p."""
    return [p[0] + d*wp[0], p[1] + d*wp[1]]

def part1(instr):
    p, h = [0, 0], 'E'
    for instr in instr:
        i, v = instr[0], instr[1]
        if i in moves:
            p = new_pos(p, i, v)
        elif i == 'R':
            h = new_heading(h, v)
        elif i == 'L':
            h = new_heading(h, -v)
        elif i == 'F':
            p = new_pos(p, h, v)
    return abs(p[0])+abs(p[1])

def part2(instr):
    wp, p = [10, 1], [0, 0]
    for instr in instr:
        i, v = instr[0], instr[1]
        if i in moves:
            wp = new_pos(wp, i, v)
        elif i == 'R':
            wp = new_wp(wp, v)
        elif i == 'L':
            wp = new_wp(wp, -v)
        elif i == 'F':
            p = new_pos_wp(p, wp, v)
    return abs(p[0])+abs(p[1])

fn = "input12.txt"
instr = []
with open(fn) as f:
    for l in f:
        m = re.match(r'(\w)(\d+)', l.strip())
        if m is not None:
            instr.append([m.group(1), int(m.group(2))])

print(part1(instr))
print(part2(instr))
