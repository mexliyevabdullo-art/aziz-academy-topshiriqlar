nums = [int(x) for x in input().split()]
t = int(input())
result = [x for x in nums if x > t]
print(*result)