n = int(input())
d = {}
for _ in range(n):
    mahsulot, son = input().split()
    d[mahsulot] = son
qidiruv = input()    
print(d.get(qidiruv, "Topilmadi"))