s = input().strip()
d = {}
for h in s:
    d[h] = d.get(h, 0) + 1
print(" ".join(f"{k}:{v}" for k, v in d.items()))    