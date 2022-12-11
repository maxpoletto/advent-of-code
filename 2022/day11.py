import re

re_monkey = re.compile(r"Monkey (\d+)")
re_start = re.compile(r"Starting items: ([\d\s,]+)")
re_op = re.compile(r"Operation: new = (.+)$")
re_div = re.compile(r"Test: divisible by (\d+)")
re_true = re.compile(r"If true: throw to monkey (\d+)$")
re_false = re.compile(r"If false: throw to monkey (\d+)$")

class Monkey:
    def __init__(self, id):
        self.id = id
        self.items = []
        self.op = ""
        self.div, self.mod = 0, 0
        self.if_true, self.if_false = 0, 0
        self.inspected = 0

    def parse(self, f):
        e = re_start.search(f.readline())
        self.items = [int(x) for x in e.group(1).split(", ")]
        e = re_op.search(f.readline())
        self.op = e.group(1)
        e = re_div.search(f.readline())
        self.div = int(e.group(1))
        e = re_true.search(f.readline())
        self.if_true = int(e.group(1))
        e = re_false.search(f.readline())
        self.if_false = int(e.group(1))

    def play(self, monkeys, part):
        l = len(self.items)
        for i in range(l):
            old = self.items.pop(0)
            new = eval(self.op)
            new = new // 3 if part == 1 else new % self.mod
            self.inspected += 1
            if new % self.div == 0:
                monkeys[self.if_true].items.append(new)
            else:
                monkeys[self.if_false].items.append(new)

def round(monkeys, part):
    for m in monkeys:
        m.play(monkeys, part)

def part(part):
    monkeys = []
    with open("input/input11.txt") as f:
        for l in f:
            e = re_monkey.search(l)
            if e:
                m = Monkey(int(e.group(1)))
                m.parse(f)
                monkeys.append(m)
    if part == 2:
        cm = 1 # common multiple of divisors
        for m in monkeys:
            cm *= m.div
        for m in monkeys:
            m.mod = cm
    n = 20 if part == 1 else 10000
    for i in range(n):
        round(monkeys, part)
    monkeys.sort(key=lambda m: m.inspected, reverse=True)
    print(monkeys[0].inspected * monkeys[1].inspected)

part(1)
part(2)
