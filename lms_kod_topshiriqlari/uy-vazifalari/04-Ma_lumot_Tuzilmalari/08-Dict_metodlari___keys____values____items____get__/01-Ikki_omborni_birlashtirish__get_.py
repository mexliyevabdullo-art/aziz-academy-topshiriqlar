total = {}
n = int(input())
for _ in range(n):
    name, miqdor = input().split()
    total[name] = total.get(name, 0) + int(miqdor)
m = int(input())
for _ in range(m):
    name, miqdor = input().split()
    total[name] = total.get(name, 0) + int(miqdor)
for name in sorted(total.keys()):
    print(name, total[name])