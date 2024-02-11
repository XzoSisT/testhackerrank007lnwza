def funnyString(x):
    a,b=[],[]
    s0=list(reversed(x))
    for i in range(len(x)-1):
        a.append(abs(ord(x[i]) - ord(x[i + 1])))
        b.append(abs(ord(s0[i]) - ord(s0[i + 1])))
    return "Funny " if a==b else "Not Funny"