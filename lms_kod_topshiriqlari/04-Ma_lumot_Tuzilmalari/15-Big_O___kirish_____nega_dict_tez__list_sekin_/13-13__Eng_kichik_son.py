# Kodingizni shu yerga yozing
import sys
data = sys.stdin.read().split()
if data:
    print(min(map(int, data[1:])))
    