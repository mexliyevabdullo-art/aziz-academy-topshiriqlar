n = int(input())
a = list(map(int, input().split()))
orta = sum(a) / n
sanoq = 0
for x in a:
    if x > orta:
        sanoq += 1
print(sanoq)        