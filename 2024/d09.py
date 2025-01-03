def read_input():
    with open("input/i09.txt") as f:
        l = list(map(int, f.readline().strip()))
        assert len(l) % 2 == 1
        return l

def part1():
    l = read_input()
    m = []
    for i, v in enumerate(l[:-1:2]):
        m += [i] * v
        m += [-1] * l[2*i+1]
    m += [len(l)//2] * l[-1]

    h, t = 0, len(m)-1
    csum = 0
    while h < t:
        while m[h] > -1 and h < t:
            csum += h*m[h]
            h += 1
        while m[t] == -1 and h < t:
            t -= 1
        while m[t] > -1 and m[h] == -1 and h < t:
            csum += h*m[t]
            m[t] = -1
            h += 1
            t -= 1
    while h < len(m):
        if m[h] > -1:
            csum += h*m[h]
        h += 1
    print(csum)

def part2():
    class Block():
        def __init__(self, pos, len, id = None):
            self.pos, self.len, self.id = pos, len, id
        def csum(self):
            return self.id * (self.pos + self.pos + self.len - 1) * self.len // 2

    l = read_input()
    pos, blocks = 0, []
    for i in range(0, len(l)-1, 2):
        blocks.append(Block(pos, l[i], i//2)) # Used block
        pos += l[i]
        blocks.append(Block(pos, l[i+1])) # Free block
        pos += l[i+1]
    blocks.append(Block(pos, l[-1], len(l)//2))

    for i in range(len(blocks)-1, -1, -2):
        for j in range(1, i, 2):
            u, f = blocks[i], blocks[j]
            if (f.len >= u.len):
                u.pos = f.pos
                f.pos += u.len
                f.len -= u.len
                break
    print(sum(block.csum() for block in blocks[::2]))

part1()
part2()
