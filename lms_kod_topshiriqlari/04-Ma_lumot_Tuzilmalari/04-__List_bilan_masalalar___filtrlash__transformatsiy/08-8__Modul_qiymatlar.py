n = int(input())
nums = list(map(int, input().split()))
result = [abs(x) for x in nums]
print(result)