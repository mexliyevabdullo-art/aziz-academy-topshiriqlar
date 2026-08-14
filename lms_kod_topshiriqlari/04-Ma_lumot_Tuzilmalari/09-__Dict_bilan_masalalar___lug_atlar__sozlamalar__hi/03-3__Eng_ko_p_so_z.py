import sys
from collections import Counter
_, *w = sys.stdin.read().split()
print(Counter(w).most_common(1)[0][0])