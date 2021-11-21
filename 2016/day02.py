from lib import aodfile
from typing import Tuple

dirs = {
    'U': ( 0,-1),
    'D': ( 0, 1),
    'L': (-1, 0),
    'R': ( 1, 0)
}

def inc(x, y, d, pad) -> Tuple[int, int]:
    dx, dy = dirs[d][0], dirs[d][1]

    if pad[y+dy][x+dx] != ".":
        x += dx
        y += dy
    return (x, y)

def solve_code(startx, starty, pad):
    x, y = startx, starty
    lines = aodfile.stripped_lines("input/input02.txt")
    code = ""
    for l in lines:
        l = l.strip()
        for c in l:
            x, y = inc(x, y, c, pad)
        code += pad[y][x]
    return code

def part1():
    pad = [
        ".....",
        ".123.",
        ".456.",
        ".789.",
        "....."
    ]
    return solve_code(2, 2, pad)

def part2():
    pad = [
        ".......",
        "...1...",
        "..234..",
        ".56789.",
        "..ABC..",
        "...D...",
        "......."
    ]
    return solve_code(2, 3, pad)

print(part1())
print(part2())
