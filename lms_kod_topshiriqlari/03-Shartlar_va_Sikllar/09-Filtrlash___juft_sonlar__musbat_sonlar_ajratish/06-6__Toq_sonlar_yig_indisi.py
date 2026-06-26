n = int(input())
a = list(map(int, input().split()))
print(sum(x for x in a if x % 2 != 0))