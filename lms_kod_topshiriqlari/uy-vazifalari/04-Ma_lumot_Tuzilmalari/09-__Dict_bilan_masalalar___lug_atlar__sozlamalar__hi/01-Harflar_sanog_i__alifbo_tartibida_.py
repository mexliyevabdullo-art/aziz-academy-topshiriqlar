s = input().strip()
for c in sorted(set(s)):
    print(c, s.count(c))