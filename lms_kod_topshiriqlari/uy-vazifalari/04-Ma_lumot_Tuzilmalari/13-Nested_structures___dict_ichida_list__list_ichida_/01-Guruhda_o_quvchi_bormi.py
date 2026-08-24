import sys
d = {}
lines = sys.stdin.read().splitlines()
n = int(lines[0])
for line in lines[1:n+1]:
    parts = line.split()
    d[parts[0]] = parts[1:]
g, name = lines[n+1].split() 
print("Ha" if name in d[g] else "Yoq")