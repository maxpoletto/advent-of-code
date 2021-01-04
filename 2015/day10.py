#!/opt/local/bin/python

def lookandsay(s):
    i, res = 0, []
    while i < len(s):
        j = i+1
        while j < len(s) and s[j] == s[i]:
            j += 1
        res += [str(j-i), s[i]]
        i = j
    return ''.join(res)

def test():
    s = "1"
    print(s)
    for _ in range(5):
        s = lookandsay(s)
        print(s)

def seq(n):
    s = "1113222113"
    for _ in range(n):
        s = lookandsay(s)
    return len(s)

print(seq(40)) # part 1
print(seq(50)) # part 2
