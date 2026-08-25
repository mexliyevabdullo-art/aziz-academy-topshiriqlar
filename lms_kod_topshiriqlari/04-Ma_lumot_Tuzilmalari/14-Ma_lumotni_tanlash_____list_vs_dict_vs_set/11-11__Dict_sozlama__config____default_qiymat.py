import sys
t = sys.stdin.read().split()
k, i = int(t[0]), 1
d = {t[i]: int(t[i+1]) for i in range(1, 2*k, 2)}
q = int(t[2*k + 1])
for key in t[2*k + 2:]:
    print(d.get(key, 0))