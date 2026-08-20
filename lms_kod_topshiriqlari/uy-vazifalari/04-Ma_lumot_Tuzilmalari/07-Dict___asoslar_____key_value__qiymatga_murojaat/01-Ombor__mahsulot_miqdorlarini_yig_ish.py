n = int(input())
d = {}
for _ in range(n):
    name, qty = input().split()
    qty = int(qty)
    if name in d:
        d[name] += qty
    else:
        d[name] = qty
for name, total in d.items():
    print(name, total)