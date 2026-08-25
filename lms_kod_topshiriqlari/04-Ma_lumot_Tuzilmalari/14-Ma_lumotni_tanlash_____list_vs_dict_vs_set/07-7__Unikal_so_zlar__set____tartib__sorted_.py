import sys
words = sys.stdin.read().split()
print(*(sorted(set(w.lower() for w in words))))
