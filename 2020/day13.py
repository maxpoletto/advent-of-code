#!/opt/local/bin/python

def part1(earliest, buses):
    """'earliest' is the earliest departure time.
    'buses' is the list of bus IDs, such that bus with ID x departs at
    times that are multiples of x.
    """
    best_bus, best_time = -1, 0
    for b in buses:
        t = b - (earliest % b)
        if t == b:
            return
        if t < best_time or best_bus < 0:
            best_time = t
            best_bus = b
    return best_bus * best_time

def part2(buses):
    """'buses' is an array of pairs. For each pair (x, y), x is a bus ID and
    y is x minus the desired offset of x's starting time from some time t (mod x).
    (In this problem, the desired offset is x's position in the bus schedule.)
    We want to find t such that t % x = y for all (x, y). All x are coprime.
    """
    inc = buses[0][0]
    res = inc
    for b in buses[1:]:
        while (True):
            if res % b[0] == b[1]:
                inc *= b[0]
                break
            res += inc
    return res

fn = "input13.txt"
with open(fn) as f:
    earliest = int(f.readline())
    schedule = f.readline().strip().split(',')
    buses = [int(x) for x in schedule if x != 'x']
    buses2 = []
    for i in range(len(schedule)):
        if schedule[i] == 'x':
            continue
        b = int(schedule[i])
        buses2.append([b, (b-i)%b])

print(part1(earliest, buses))
print(part2(buses2))
