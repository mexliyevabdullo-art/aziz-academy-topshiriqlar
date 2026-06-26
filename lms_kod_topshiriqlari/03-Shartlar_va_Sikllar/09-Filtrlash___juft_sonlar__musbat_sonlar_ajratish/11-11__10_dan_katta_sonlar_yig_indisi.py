n = int(input())
sonlar = list(map(int, input().split()))
yigindi = 0
for son in sonlar:
    if son >10:
        yigindi += son
print(yigindi)        