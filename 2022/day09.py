def move(d, h, t, state):
    h = (h[0] + d[0], h[1] + d[1])
    if t[1] == h[1]: # same y
        if t[0] < h[0] - 1:
            t = (t[0]+1, t[1])
        elif t[0] > h[0] + 1:
            t = (t[0]-1, t[1])
    elif t[0] == h[0]: # same x
        if t[1] < h[1] - 1:
            t = (t[0], t[1]+1)
        elif t[1] > h[1] + 1:
            t = (t[0], t[1]-1)
    else: # diagonal
        if t[0] < h[0] and t[1] < h[1] and (t[0] < h[0] - 1 or t[1] < h[1] - 1):
            t = (t[0]+1, t[1]+1)
        elif t[0] > h[0] and t[1] > h[1] and (t[0] > h[0] + 1 or t[1] > h[1] + 1):
            t = (t[0]-1, t[1]-1)
        elif t[0] < h[0] and t[1] > h[1] and (t[0] < h[0] - 1 or t[1] > h[1] + 1):
            t = (t[0]+1, t[1]-1)
        elif t[0] > h[0] and t[1] < h[1] and (t[0] > h[0] + 1 or t[1] < h[1] - 1):
            t = (t[0]-1, t[1]+1)
    if state:
        state.add(t)
    return h, t
"""
         if t[0] < h[0] - 1:
            t = (t[0]+1, h[1])
        elif t[0] > h[0] + 1:
            t = (t[0]-1, h[1])
        elif t[1] < h[1] - 1:
            t = (h[0], t[1]+1)
        elif t[1] > h[1] + 1:
            t = (h[0], t[1]-1)
 """

def move_rope(d, r, state):
    r[0] = (r[0][0] + d[0], r[0][1] + d[1])
    for i in range(1, len(r)):
        r[i-1], r[i] = move((0, 0), r[i-1], r[i], None)
    state.add(r[9])

def part1():
    h, t = (0,0), (0,0)
    state = { t }
    with open("input/input09.txt") as f:
#    with open("input/yy") as f:
        for l in f:
            dir, dist = l.strip().split()
            dist = int(dist)
            if dir == "R":
                d = (1, 0)
            elif dir == "L":
                d = (-1, 0)
            elif dir == "U":
                d = (0, 1)
            elif dir == "D":
                d = (0, -1)
            for i in range(dist):
                h, t = move(d, h, t, state)
            #print(dist, dir, state)
    print(len(state))

#2604 high
def part2():
    rope = [ (0,0) for i in range(10) ]
    state = { rope[9] }
    with open("input/input09.txt") as f:
#    with open("input/yy") as f:
        for l in f:
            dir, dist = l.strip().split()
            dist = int(dist)
            if dir == "R":
                d = (1, 0)
            elif dir == "L":
                d = (-1, 0)
            elif dir == "U":
                d = (0, 1)
            elif dir == "D":
                d = (0, -1)
            for i in range(dist):
                move_rope(d, rope, state)
    print(len(state))

part1()
part2()
