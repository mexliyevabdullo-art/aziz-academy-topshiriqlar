n = int(input())
sonlar = list(map(int, input().split()))
nat = [x**2 for x in sonlar if x % 2 != 0]
print(nat)