n = int(input())
numbers = list(map(int, input() .split()))
toq_sonlar = [x for x in numbers if x % 2 != 0]
print(toq_sonlar)