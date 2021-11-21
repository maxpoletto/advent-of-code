from lib import aodfile

def part1():
    dirs = [(0,1), (1,0), (0, -1), (-1,0)]
    d, x, y = 0, 0, 0
    insts = aodfile.comma_separated("input/input01.txt")
    for i in insts:
        if i[0] == 'R':
            d = (d+1)%4
        else:
            d = (d-1)%4
        l = int(i[1:])
        x, y = x+l*dirs[d][0], y+l*dirs[d][1]
    return abs(x)+abs(y)

def part2():
    dirs = [(0,1), (1,0), (0, -1), (-1,0)]
    d, x, y = 0, 0, 0
    insts = aodfile.comma_separated("input/input01.txt")
    visited = {}
    revisited = False
    for i in insts:
        if i[0] == 'R':
            d = (d+1)%4
        else:
            d = (d-1)%4
        l = int(i[1:])
        for j in range(0, l):
            x, y = x+dirs[d][0], y+dirs[d][1]
            t = (x, y)
            if t in visited.keys():
                revisited = True
                break
            visited[t] = True
        if revisited:
            break
    return abs(x)+abs(y)

print(part1())
print(part2())
