#!/opt/local/bin/python

def match(rules, id, message, pos):
    """Matches rule #id against message starting at position pos.
    If rule consumes message up to position n, returns (True, n+1).
    Otherwise, returns (False, pos).
    """
    if pos >= len(message):
        return False, pos
    if rules[id] == 'a' or rules[id] == 'b':
        return message[pos] == rules[id], pos+1
    for opt in rules[id]:
        matched = True
        p = pos
        for t in opt:
            ok, np = match(rules, t, message, p)
            if not ok:
                matched = False
                continue
            p = np
        if matched:
            return True, p
    return False, pos

def fullmatch(rules, id, message):
    """Returns true if rule #id fully consumes message."""
    ok, pos = match(rules, id, message, 0)
    return ok and pos == len(message)

def specialmatch(rules, message):
    """Returns true if message matches (rule 42){m}(rule 31){n},
    where m > 1 and n > m.
    """
    e42 = []
    pos = 0
    while True:
        ok, pos = match(rules, '42', message, pos)
        if not ok:
            break
        e42.append(pos)
    for i in range(1, len(e42)):
        pos = e42[i]
        n42, n31 = i+1, 0
        while True:
            ok, pos = match(rules, '31', message, pos)
            if not ok:
                break
            n31 += 1
            if pos == len(message) and n42 > n31:
                return True
    return False

def part1(rules, messages):
    n = 0
    for m in messages:
        if fullmatch(rules, '0', m):
            n += 1
    return n

def part2(rules, messages):
    rules['8'] = [['42'], ['42','8']]
    rules['11'] = [['42','31'], ['42','11','31']]
    n = 0
    for m in messages:
        if specialmatch(rules, m):
            n += 1
    return n

fn = "input19.txt"
rules = {}
messages = []
with open(fn) as f:
    for l in f:
        l = l.strip()
        if len(l) == 0:
            continue
        if l[0] == 'a' or l[0] == 'b':
            messages.append(l)
            continue
        id, exp = l.split(':')
        exp = exp.strip()
        if exp == '"a"' or exp == '"b"':
            rules[id] = exp[1]
            continue
        rules[id] = []
        exps = exp.split('|')
        for exp in exps:
            e = exp.strip().split(' ')
            rules[id].append(e)

print(part1(rules,messages))
print(part2(rules,messages))
