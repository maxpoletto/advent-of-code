#!/opt/local/bin/python

class Game:
    """Implements the crab cup game."""
    def __init__(self, cups):
        self.next = [0]*(1+len(cups))
        first = cups[0]
        n = self.next
        for i in range(len(cups)-1):
            n[cups[i]] = cups[i+1]
        n[cups[-1]] = first
        self.curr = first
        self.max = len(cups)
    def play(self, rounds):
        """Plays the given number of rounds of the cup game."""
        n, curr = self.next, self.curr # object dereferences are expensive
        for _ in range(rounds):
            a = n[curr]
            b = n[a]
            c = n[b]
            d = curr-1
            if d < 1:
                d = self.max
            while (a == d or b == d or c == d):
                d -= 1
                if d < 1:
                    d = self.max
            e = n[c]
            n[curr] = e
            curr = e
            n[c] = n[d]
            n[d] = a
        self.curr = curr
    def after(self, l, n = -1):
        """Prints the n cups clockwise from the cup labeled l
        (or all cups (except l) if n < 0).
        """
        p = l
        res = []
        if n < 0:
            n = self.max-1
        for _ in range(n):
            p = self.next[p]
            res.append(p)
        return res

def part1():
    cups = "653427918"
    game = Game([int(x) for x in cups])
    game.play(100)
    return "".join([str(x) for x in game.after(1)])

def part2():
    cups = "653427918"
    n, rounds = 1000*1000, 10*1000*1000
    c = [int(x) for x in cups] + [x for x in range(10,n+1)]
    game = Game(c)
    game.play(rounds)
    res = game.after(1,2)
    return res[0] * res[1]

print(part1())
print(part2())
