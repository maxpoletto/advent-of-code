def part1():
    succ = {}
    tot = 0
    with open("input/i05.txt") as f:
        for l in f:
            l = l.strip()
            if l == "":
                continue
            if l.count('|') == 1:
                a, b = map(int, l.split('|'))
                succ.setdefault(a, set()).add(b)
                continue
            pp = list(map(int, l.split(',')))
            seen = set()
            bad = False
            for p in pp:
                if p in succ:
                    for s in succ[p]:
                        if s in seen:
                            bad = True
                            break
                if bad:
                    break
                seen.add(p)
            if not bad:
                tot += pp[len(pp)//2]
    print(tot)

def part2():
    succ = {}
    tot = 0
    with open("input/i05.txt") as f:
        for l in f:
            l = l.strip()
            if l == "":
                continue
            if l.count('|') == 1:
                a, b = map(int, l.split('|'))
                succ.setdefault(a, set()).add(b)
                continue
            pp = list(map(int, l.split(',')))
            nreorders = 0
            while (True):
                seen = {}
                reorder = False
                for i in range(len(pp)):
                    p = pp[i]
                    if p in succ:
                        for s in succ[p]:
                            if s in seen:
                                j = seen[s]
                                pp = pp[:j] + [p] + pp[j:i] + pp[i+1:]
                                reorder = True
                                nreorders += 1
                                break
                    if reorder:
                        break 
                    seen[p] = i
                if not reorder:
                    if nreorders > 0:
                        tot += pp[len(pp)//2]
                    break
    print(tot)

part1()
part2()
