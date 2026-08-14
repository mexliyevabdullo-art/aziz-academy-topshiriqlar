# Kodingizni shu yerga yozing
import sys
from collections import Counter
s = sys.stdin.read().strip()
print(max(Counter(s).items(), key=lambda x: (x[1], -s.index(x[0])))[0])