sonlar = map(int, input().split())
juftlar = [x for x in sonlar if x % 2 == 0]
print(*juftlar)