import re
from lib import aodfile, mat

def run():
    screen = [ ['.'] * 50 for i in range(6)] 
    lines = aodfile.stripped_lines("input/input08.txt")
    for l in lines:
        m = re.match('rect (\d+)x(\d+)', l)
        if m:
            mat.set(screen, 0, 0, int(m.group(2))-1, int(m.group(1))-1, '#')
            continue
        m = re.match('rotate row y=(\d+) by (\d+)', l)
        if m:
            mat.rotate_row(screen, int(m.group(1)), int(m.group(2)))
            continue
        m = re.match('rotate column x=(\d+) by (\d+)', l)
        if m:
            mat.rotate_col(screen, int(m.group(1)), int(m.group(2)))
            continue
    cnt = 0
    for r in range(len(screen)):
        for c in range(len(screen[0])):
            if screen[r][c] == '#':
                cnt += 1
    print(cnt)
    print(mat.pp(screen))

run()

