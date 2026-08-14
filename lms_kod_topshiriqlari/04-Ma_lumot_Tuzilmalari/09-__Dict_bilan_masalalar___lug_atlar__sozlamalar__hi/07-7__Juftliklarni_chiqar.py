# Kodingizni shu yerga yozing
import sys
_, *l = sys.stdin.read().split()
for i in range(0, len(l), 2):
    print(f"{l[i]}={l[i+1]}")