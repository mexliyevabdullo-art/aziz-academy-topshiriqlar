import sys
data = sys.stdin.read().split()
if data:
    unique_numbers = sorted(set(map(int, data[1:])))
    print(*(unique_numbers))