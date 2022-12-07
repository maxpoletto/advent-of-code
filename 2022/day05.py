def move_creates(reverse):
    """read every line in input04.txt"""
    pos = [1, 5, 9, 13, 17, 21, 25, 29, 33]
    stack = [ "" ] * 9
    insts = []
    with open("input/input05.txt") as f:
        for l in f:
            if l.find('[') >= 0:
                for i in range(9):
                    if l[pos[i]] != ' ':
                        stack[i] = stack[i] + l[pos[i]]
                continue
            if l.find('move') >= 0:
                l = l.split()
                insts.append((int(l[1]), int(l[3])-1, int(l[5])-1))
    for i in insts:
        t = stack[i[1]][0:i[0]]
        if reverse:
            t = t[::-1]
        stack[i[1]] = stack[i[1]][i[0]:]
        stack[i[2]] = t + stack[i[2]]
    print(''.join([ stack[i][0] for i in range(9) ]))

# part1
move_creates(True)
# part2
move_creates(False)
