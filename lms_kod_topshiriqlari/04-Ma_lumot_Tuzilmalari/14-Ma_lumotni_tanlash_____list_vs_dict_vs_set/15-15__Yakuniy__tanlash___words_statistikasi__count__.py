import sys
from collections import Counter
w = sys.stdin.read().split()
c = Counter(x.lower() for x in w)
top = min(c, key=lambda x: (-c[x], x)) if c else 0
print(f"total: {len(w)}\nunique: {len(c)}\ntop: {top} {c.get(top, 0)}")