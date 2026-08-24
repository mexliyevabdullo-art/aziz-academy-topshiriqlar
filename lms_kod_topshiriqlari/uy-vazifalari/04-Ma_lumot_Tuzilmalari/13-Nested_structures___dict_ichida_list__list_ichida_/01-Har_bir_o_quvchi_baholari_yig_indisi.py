import sys
l = []
lines = sys.stdin.read().splitlines()
for line in lines[1:]:
    p = line.split()
    l.append({"name": p[0], "grades": [int(x) for x in p[1:]]})
for s in l:
    print(s["name"], sum(s["grades"]))