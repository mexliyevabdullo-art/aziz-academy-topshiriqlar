import sys
from collections import Counter
words = [w.lower() for w in sys.stdin.read().split()]
if words:
    c = Counter(words)
    best = min(c.keys(), key=lambda x: (-c[x], x))
    print(best, c[best])