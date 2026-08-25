import sys
print(*(sorted({len(w) for w in sys.stdin.read().split()})))