def findblock(sz):
    insts = []
    with open("input/input06.txt") as f:
        l = f.readline()
        for i in range(sz-1, len(l)):
            s = {}
            for j in range(i+1-sz, i+1):
                s[l[j]] = True
            if len(s) == sz:
                print(i+1)
                break

# part 1
findblock(4)
# part 2
findblock(14)

