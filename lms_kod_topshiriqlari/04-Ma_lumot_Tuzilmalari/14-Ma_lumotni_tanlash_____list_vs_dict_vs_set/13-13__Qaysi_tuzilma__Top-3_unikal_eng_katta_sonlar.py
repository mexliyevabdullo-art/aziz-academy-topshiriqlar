import sys
nums = sorted(set(map(int, sys.stdin.read().split())), reverse=True)
print(*(nums[:3]))