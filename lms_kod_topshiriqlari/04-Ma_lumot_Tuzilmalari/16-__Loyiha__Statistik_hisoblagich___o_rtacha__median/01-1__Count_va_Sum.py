import sys
data = sys.stdin.read().split()
if data:
    nums = [int(x) for x in data]
    print(len(nums))
    print(sum(nums))