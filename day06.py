#!/opt/local/bin/python

def count(d, n):
    """Returns number of keys in d that have value n."""
    return sum([(d[i] == n) for i in d])

def part1(groups):
    """Number of distinct groups per group."""
    return sum([len(x) for x in groups])

def part2(groups, npeople):
    return sum([count(groups[i], npeople[i]) for i in range(len(groups))])

fn = "input06.txt"
groups, npeople = [], [] # groups of questions, number of people per group
n, d = 0, {}
with open(fn) as f:
    for l in f:
        l = l.strip()
        if len(l) == 0:
            groups.append(d)
            npeople.append(n)
            n, d = 0, {}
        else:
            n += 1
            for c in l:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
    if n > 0:
        groups.append(d)
        npeople.append(n)

print(part1(groups))
print(part2(groups, npeople))
