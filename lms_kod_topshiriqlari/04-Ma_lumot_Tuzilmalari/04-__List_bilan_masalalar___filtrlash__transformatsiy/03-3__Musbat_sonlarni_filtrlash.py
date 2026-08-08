n = int(input())
numbers = list(map(int, input().split()))
musbat_sonlar = [x for x in numbers if x > 0]
print(musbat_sonlar)