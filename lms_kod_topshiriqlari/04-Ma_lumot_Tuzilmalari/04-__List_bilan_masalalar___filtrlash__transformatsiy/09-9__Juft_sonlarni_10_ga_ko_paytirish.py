n = int(input())
nums = list(map(int, input().split()))
result = [x * 10 for x in nums if x % 2 == 0]
print((result))