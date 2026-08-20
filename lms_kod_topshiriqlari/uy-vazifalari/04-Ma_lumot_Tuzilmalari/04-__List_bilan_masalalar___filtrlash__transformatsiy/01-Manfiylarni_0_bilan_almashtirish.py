nums = [int(x) for x in input().split()]
result = [0 if x < 0 else x for x in nums]
print(*result)