n = int(input())
sonlar = list(map(int, input().split()))
for son in sonlar:
    if son % 2 == 0 or son < 0:
        print(son)      