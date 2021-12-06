from lib import aodfile

def fish(days):
    fish = [0]*9
    for f in map(lambda x: int(x), aodfile.comma_separated("input/input06.txt")):
        fish[f] += 1
    for i in range(days):
        n = fish[0]
        for f in range(1, len(fish)):
            fish[f-1] = fish[f]
        fish[6] += n
        fish[8] = n
    print(sum(fish))

fish(80)
fish(256)
