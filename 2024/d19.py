from functools import cache

def read_input():
    with open("input/i19.txt") as f:
        p, d = f.read().split("\n\n")
        return p.split(', '), d.splitlines()

def part1():
    @cache
    def possible(design):
        if design in patterns:
            return True
        for p in patterns:
            if design.startswith(p) and possible(design[len(p):]):
                return True
        return False

    patterns, designs = read_input()
    print(sum(1 for d in designs if possible(d)))

def part2():
    @cache
    def ways(design):
        n = 0
        if design in patterns:
            n = sum(1 for p in patterns if p == design)
        for p in patterns:
            if design.startswith(p) and len(p) < len(design):
                n += ways(design[len(p):])
        return n

    patterns, designs = read_input()
    print(sum(ways(d) for d in designs))

part1()
part2()
