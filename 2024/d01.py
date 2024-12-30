def part1():
    m, n = [], []
    with open("input/i01.txt") as f:
        for l in f:
            l = l.strip()
            a, b = l.split()
            m.append(int(a))
            n.append(int(b))
        m.sort()
        n.sort()
        t = 0
        for i in range(len(m)):
            t += abs(m[i] - n[i])
        print(t)

def part2():
    m = []
    n = {}
    with open("input/i01.txt") as f:
        for l in f:
            l = l.strip()
            a, b = l.split()
            m.append(int(a))
            n[int(b)] = n.get(int(b), 0) + 1
        m.sort()
        s = 0
        for i in range(len(m)):
            s += m[i] * n.get(m[i], 0)
        print(s)

part1()
part2()
