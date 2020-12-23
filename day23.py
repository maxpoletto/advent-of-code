#!/opt/local/bin/python

class Game:
    """Implements the crab cup game."""
    def __init__(self, cups):
        self.labels = cups
        self.next = cups.copy()
        self.pos = cups.copy()
        for i in range(0, len(cups)):
            self.next[i] = (i+1)%len(cups)
            self.pos[self.labels[i]-1] = i
        self.curr = 0
        self.min_label = 1
        self.max_label = len(cups)
        self.picked = [0]*3
    def pick3(self):
        """Removes from the ring the 3 cups clockwise from the current one."""
        p = self.curr
        for i in range(3):
            p = self.next[p]
            self.picked[i] = p
        self.next[self.curr] = self.next[p]
        self.next[p] = -1
    def dest_label(self):
        """Finds the label of the new destination cup."""
        label = self.labels[self.curr]-1
        while True:
            if label < self.min_label:
                label = self.max_label
            for p in self.picked:
                if label == self.labels[p]:
                    label -= 1
                    break
            else:
                break
        return label
    def play(self, rounds):
        """Plays the given number of rounds of the cup game."""
        for _ in range(rounds):
            # Remove 3 cups clockwise of the current cup.
            self.pick3()
            # Find the position of the new destination cup.
            dest = self.pos[self.dest_label()-1]
            # Insert the picked cups clockwise of the destination cup.
            self.next[self.picked[2]] = self.next[dest]
            self.next[dest] = self.picked[0]
            # Select the new current cup.
            self.curr = self.next[self.curr]
    def after(self, l, n = -1):
        """Prints the n cups clockwise from the cup labeled l
        (or all cups (except l) if n < 0).
        """
        if n < 0:
            n = len(self.labels)-1
        p = self.curr
        while self.labels[p] != l:
            p = self.next[p]
        res = []
        for _ in range(n):
            p = self.next[p]
            res.append(self.labels[p])
        return res
    def __str__(self):
        res, c = [], self.curr
        for _ in range(len(self.labels)):
            res.append(str(self.labels[c]))
            c = self.next[c]
        return " ".join(res)

def part1():
    cups = "653427918"
    game = Game([int(x) for x in cups])
    game.play(100)
    return "".join([str(x) for x in game.after(1)])

def part2():
    cups = "653427918"
    n, rounds = 1000*1000+1, 10*1000*1000
    c = [int(x) for x in cups] + [x for x in range(10,n)]
    game = Game(c)
    game.play(rounds)
    res = game.after(1,2)
    return res[0] * res[1]

print(part1())
print(part2())
