# Kodingizni shu yerga yozing
import sys
from collections import Counter
_, *w, k = sys.stdin.read().split()
print(Counter(w)[k])