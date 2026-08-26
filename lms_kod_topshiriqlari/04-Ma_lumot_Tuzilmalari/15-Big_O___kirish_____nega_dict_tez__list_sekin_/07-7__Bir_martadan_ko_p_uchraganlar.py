from collections import Counter
nums = input().split()
counts = Counter(nums)
resutl = sum(1 for count in counts.values() if count > 1)
print(resutl)