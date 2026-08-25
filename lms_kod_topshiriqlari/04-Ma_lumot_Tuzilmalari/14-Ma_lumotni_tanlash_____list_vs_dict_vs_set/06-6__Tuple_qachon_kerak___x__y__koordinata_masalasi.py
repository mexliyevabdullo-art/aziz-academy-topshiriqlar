import sys
data = sys.stdin.read().split()
points = [(int(data[i]), int(data[i+1])) for i in range(1, len(data), 2)]
best = max(points, key=lambda p: (p[0], -p[1]))
print(f"{best[0]} {best[1]}")