n = int(input())
d = {}

for _ in range(n):
    mahsulot, narx = input().split()
    d[mahsulot] = int(narx)
    
print(sum(d.values()))