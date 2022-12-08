def part1():
    pos, score = [3,4], [0, 0]
    dice, dicerolls = 0, 0
    def turn(i):
        nonlocal dice, dicerolls, score, pos
        pos[i] = (pos[i] + dice + (dice+1)%100 + (dice+2)%100 + 3)%10
        dice = (dice+3)%100
        dicerolls += 3
        score[i] = score[i] + pos[i] + 1
        if score[i] >= 1000:
            print(score[1-i]*dicerolls)
            return True
        return False
    while not turn(0) and not turn(1):
        pass

inc = { 3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1 }
tot = [0, 0]
def move(state, player):
    change = False
    state2 = {}
    pidx = 2*player
    for i in state.keys():
        if i[1] >= 21:
            tot[0] += state[i]
        elif i[3] >= 21:
            tot[1] += state[i]
        else:
            change = True
            for j in inc.keys():
                pos = (i[pidx]+j) % 10
                pts = i[1+pidx] + pos + 1
                if player == 0:
                    s = (pos, pts, i[2], i[3])
                else:
                    s = (i[0], i[1], pos, pts)
                state2[s] = state2.get(s, 0) + state[i]*inc[j]
    return change, state2

def part2():
    state = {}
    # state is (pos0, score0, pos1, score1)
    state[(3, 0, 4, 0)] = 1
    change = True
    while change:
        change, state = move(state, 0) # Turn for player 0
        if not change:
            break
        change, state = move(state, 1) # Turn for player 1
    print(tot[0], tot[1])

part1()
part2()
