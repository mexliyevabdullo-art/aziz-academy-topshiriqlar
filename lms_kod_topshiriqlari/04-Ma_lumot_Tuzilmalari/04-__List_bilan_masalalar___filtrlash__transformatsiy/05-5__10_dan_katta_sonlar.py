n = int(input())
sonlar = list(map(int, input().split()))
natija = []
for son in sonlar:
    if son > 10:
        natija.append(son)
print(natija)        