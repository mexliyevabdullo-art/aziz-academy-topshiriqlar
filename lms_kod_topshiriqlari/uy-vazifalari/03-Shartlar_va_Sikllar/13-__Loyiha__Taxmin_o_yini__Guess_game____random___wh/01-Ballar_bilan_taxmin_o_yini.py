import sys
s, *t = map(int, sys.stdin.read().split())
b = 100
for x in t:
    print("KATTA" if x > s else "KICHIK" if x < s else "TOPDINGIZ")
    if x == s: break
    b = max(0, b - 10)
print(f"Ball: {b}")