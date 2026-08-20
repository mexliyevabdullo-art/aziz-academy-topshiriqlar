nums = list(map(int, input().split()))
copied_nums = nums[:]
copied_nums.sort()
print(*nums)
print(*copied_nums)