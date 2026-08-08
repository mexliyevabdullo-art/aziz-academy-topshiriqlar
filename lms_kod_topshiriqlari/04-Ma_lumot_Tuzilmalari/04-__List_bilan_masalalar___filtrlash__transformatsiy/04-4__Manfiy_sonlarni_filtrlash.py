n = int(input())
numbers = list(map(int, input().split()))
manfiy_sonlar = [x for x in numbers if x < 0]
print(manfiy_sonlar)