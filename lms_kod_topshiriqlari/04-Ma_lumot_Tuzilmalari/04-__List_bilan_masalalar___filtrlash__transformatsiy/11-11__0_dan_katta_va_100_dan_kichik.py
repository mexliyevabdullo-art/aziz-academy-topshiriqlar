n = int(input())
sonlar = list(map(int, input().split()))
nat = [x for x in sonlar if 0 < x < 100]
print(nat)