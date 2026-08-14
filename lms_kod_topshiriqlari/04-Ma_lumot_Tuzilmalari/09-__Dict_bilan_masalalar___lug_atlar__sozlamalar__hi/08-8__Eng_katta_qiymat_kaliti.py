# Kodingizni shu yerga yozing
import sys
_, *l = sys.stdin.read().split()
print(max(zip(l[::2], map(int, l[1::2])), key=lambda x: x[1])[0])
      