import sys
lines = sys.stdin.read().splitlines()
d = {}
for line in lines[1:]:
    p = line.split()
    d[p[0]] = p[1:]
print(max(d, key=lambda x: len(d[x])))    