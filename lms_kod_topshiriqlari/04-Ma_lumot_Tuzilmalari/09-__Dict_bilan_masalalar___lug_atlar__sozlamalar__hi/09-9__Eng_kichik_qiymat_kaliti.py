# Kodingizni shu yerga yozing
import sys
_, *l = sys.stdin.read().split()
print(min(zip(l[0::2], map(int, l[1::2])), key=lambda x: (x[1], l[0::2].index(x[0])))[0])