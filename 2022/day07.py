import pprint

def compsz(dir):
    s = 0
    for d in dir['d'].values():
        s += compsz(d)
    for f in dir['f'].values():
        s += f
    dir['sz'] = s
    return s

def buildfs():
    fs = { '..': None, 'd': {}, 'f': {}, 'sz': 0 }
    cwd = fs
    with open("input/input07.txt") as f:
        for l in f:
            if l.startswith("$ cd "):
                d = l[5:-1]
                if d == "/":
                    cwd = fs
                elif d == "..":
                    cwd = cwd['..']
                else:
                    if d not in cwd['d']:
                        cwd['d'][d] = { '..': cwd, 'd': {}, 'f': {}, 'sz': 0 }
                    cwd = cwd['d'][d]
            elif l.startswith("$ ls") or l.startswith("dir"):
                continue
            else:
                sz, name = l.split()
                cwd['f'][name] = int(sz)
    compsz(fs)
    return fs

def part1():
    fs = buildfs()
    q = [fs]
    tot = 0
    while q:
        d = q.pop()
        for k in d['d'].values():
            q.append(k)
        if d['sz'] <= 100000:
            tot += d['sz']
    print(tot)

def part2():
    fs = buildfs()
    target = 30000000 - (70000000 - fs['sz'])
    if target <= 0:
        print(target)
        return
    q = [fs]
    smallest = 70000000
    while q:
        d = q.pop()
        for k in d['d'].values():
            q.append(k)
        if d['sz'] >= target and d['sz'] < smallest:
            smallest = d['sz']
    print(smallest)

part1()
part2()
