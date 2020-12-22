#!/opt/local/bin/python

import re

class Player:
    def __init__(self, id, cards):
        self.id = id
        self.history = {}
        self.cards = cards.copy()
    def copy(self, num_cards):
        return Player(self.id, self.cards[:num_cards])
    def cards_already_seen(self):
        return str(self.cards) in self.history
    def set_history(self):
        self.history[str(self.cards)] = True
    def pick_card(self):
        c = self.cards[0]
        self.cards = self.cards[1:]
        return c
    def add_cards(self, cards):
        self.cards += cards
    def num_cards(self):
        return len(self.cards)
    def score(self):
        mul, res = 1, 0
        for i in range(len(self.cards)-1, -1, -1):
            res += self.cards[i] * mul
            mul += 1
        return res
    def __str__(self):
        return str(self.id) + ":" + str(self.cards)

def recursive_combat(player1, player2):
    while player1.num_cards() > 0 and player2.num_cards() > 0:
        if player1.cards_already_seen() or player2.cards_already_seen():
            return player1
        player1.set_history()
        player2.set_history()
        c1 = player1.pick_card()
        c2 = player2.pick_card()
        if player1.num_cards() >= c1 and player2.num_cards() >= c2:
            winner = recursive_combat(player1.copy(c1), player2.copy(c2))
            if winner.id == 1:
                player1.add_cards([c1,c2])
            else:
                player2.add_cards([c2,c1])
        else:
            if c1 > c2:
                player1.add_cards([c1,c2])
            else:
                player2.add_cards([c2,c1])
    if player1.num_cards() > 0:
        return player1
    return player2

def part1(cards):
    player1 = Player(1, cards[0])
    player2 = Player(2, cards[1])
    while player1.num_cards() > 0 and player2.num_cards() > 0:
        c1 = player1.pick_card()
        c2 = player2.pick_card()
        if c1 > c2:
            player1.add_cards([c1, c2])
        else:
            player2.add_cards([c2, c1])
    if player1.num_cards() > 0:
        return player1.score()
    return player2.score()

def part2(cards):
    player1 = Player(1, cards[0])
    player2 = Player(2, cards[1])
    winner = recursive_combat(player1, player2)
    return winner.score()

fn = "input22.txt"
with open(fn) as f:
    cards = [[],[]]
    p = 0
    for l in f:
        l = l.strip()
        if len(l) == 0:
            continue
        m = re.match(r'Player (\d):', l)
        if m:
            p = int(m.group(1))-1
            continue
        cards[p].append(int(l))
print(part1(cards))
print(part2(cards))
