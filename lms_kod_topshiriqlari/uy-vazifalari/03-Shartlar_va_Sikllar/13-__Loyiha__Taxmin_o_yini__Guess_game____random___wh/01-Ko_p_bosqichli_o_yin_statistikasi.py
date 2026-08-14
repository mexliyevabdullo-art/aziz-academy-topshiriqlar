import sys 
d = sys.stdin.read().split()
i, t, m = 1, 0, 1e9
for r in range(1, int(d[0]) + 1):
    tg, a = d[i], 0
    while d[i := i + 1] != tg: a += 1
    i, a = i + 1, a + 1
    print(f"Round {r}: {a} urinish")
    t, m = t + a, min(m, a)
print(f"Jami: {t}\nEng yaxshi: {m}")
    