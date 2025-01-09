def read_input():
    locks, keys = {}, {}
    with open('input/i25.txt') as f:
        blocks = f.read().split('\n\n')
        for b in blocks:
            l = b.strip().split('\n')
            v = [ 0 ] * 5
            for r in range(1, len(l) - 1):
                for c in range(0, len(l[r])):
                    if l[r][c] == '#':
                        v[c] += 1
            if l[0] == '#####':
                locks.append(v)
            else:
                keys.append(v)
    return locks, keys

def part1():
    locks, keys = read_input()
    n = 0
    for l in locks:
        for k in keys:
            if all([ a < 6 for a in map(sum, zip(l, k))]):
                n += 1            
            print(all([ a < 6 for a in map(sum, zip(l, k))]))
    print(locks)
    print(keys)
    print(n)

part1()
