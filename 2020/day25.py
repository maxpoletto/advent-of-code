#!/usr/local/bin/python

class Peer:
    def __init__(self, pub):
        self.pub = pub
        val, ls = 1, 0
        while val != pub:
            ls += 1
            val = (val * 7) % 20201227
        self.priv = ls
    def ek(self, pub):
        val = 1
        for _ in range(self.priv):
            val = (val * pub) % 20201227
        return val

pubs = [6270530, 14540258]
peer = [Peer(p) for p in pubs]
ans = []
for i in range(len(peer)):
    ans.append(peer[i].ek(peer[1-i].pub))
assert(ans[0] == ans[1])
print(ans[0])
