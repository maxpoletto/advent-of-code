#!/opt/local/bin/python

import re

def in_intervals(intervals, val):
    """Returns true if val falls within any of the given [start, end] intervals."""
    for i in intervals:
        if val >= i[0] and val <= i[1]:
            return True
    return False
            
def meets_rules(rules, ticket):
    """Returns true if every field in ticket falls within an interval given by one of the rules."""
    for val in ticket:
        ok = False
        for r in rules:
            if in_intervals(rules[r], val):
                ok = True
                break
        if not ok:
            return False
    return True

def part1(tickets, rules):
    tot = 0
    for ticket in tickets:
        for val in ticket:
            ok = False
            for r in rules:
                if in_intervals(rules[r], val):
                    ok = True
                    break
            if not ok:
                tot += val
    return tot

def part2(tickets, myticket, rules):
    valid_tickets = [t for t in tickets if meets_rules(rules, t)]
    # For every ticket position, find what rules it matches.
    possible = []
    for i in range(len(myticket)):
        bad_fields = {}
        for ticket in valid_tickets:
            for r in rules:
                if not in_intervals(rules[r], ticket[i]):
                    bad_fields[r] = True
                    break
        ok_fields = {}
        for r in rules:
            if r not in bad_fields:
                ok_fields[r] = True
        possible.append([i, ok_fields])
    # Sort positions from most constrained (matches 1 rule) to least.
    possible.sort(key = lambda x: len(x[1]))
    # Process of elimination to find one rule per position.
    consumed = {}
    for poss in possible:
        for c in consumed:
            del poss[1][c]
        for p in poss[1]:
            consumed[p] = True
    possible.sort(key = lambda x: x[0])
    # Ordered list of fields.
    fields = [ list(poss[1].keys())[0] for poss in possible]
    # Now we have all the information to answer the puzzle question.
    ans = 1
    for i in range(len(myticket)):
        if fields[i].startswith("departure"):
            ans *= myticket[i]
    return ans

fn = "input16.txt"
rules = {}
tickets = []
with open(fn) as f:
    l = f.readline()
    while len(l) > 0 and l != "your ticket:\n":
        m = re.match(r'([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)', l)
        if m is not None:
            field = m.group(1)
            rules[field] = [ (int(m.group(2)), int(m.group(3))),
                             (int(m.group(4)), int(m.group(5))) ]
        l = f.readline()
    l = f.readline()
    myticket = [int(x) for x in l.strip().split(',')]
    l = f.readline() # skip blank
    l = f.readline() # skip "nearby tickets:"
    l = f.readline()
    while len(l) > 0:
        tickets.append([int(x) for x in l.strip().split(',')])
        l = f.readline()

print(part1(tickets, rules))
print(part2(tickets, myticket, rules))
