n = int(input())
sonlar = list(map(int, input().split()))
maks = sonlar[0]
for i in range(1, n):
    if sonlar[i] > maks :
        maks = sonlar[i]
print(maks)        