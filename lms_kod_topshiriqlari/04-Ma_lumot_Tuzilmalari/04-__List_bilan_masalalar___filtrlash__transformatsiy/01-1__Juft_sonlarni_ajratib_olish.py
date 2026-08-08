n = int(input())
numbers = list(map(int, input().split()))
juft_sonlar = [x for x in numbers if x % 2 == 0]
print(juft_sonlar)