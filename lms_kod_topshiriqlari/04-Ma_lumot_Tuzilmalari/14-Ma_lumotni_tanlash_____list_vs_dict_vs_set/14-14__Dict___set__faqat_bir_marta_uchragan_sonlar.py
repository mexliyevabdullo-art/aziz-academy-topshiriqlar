import sys
from collections import Counter
nums = sys.stdin.read().split()
if not nums:
    print("EMPTY")
else:
    c = Counter(nums)
    res = sorted([x for x, count in c.items() if count == 1], key=int)
    if res:
        print(*res)
    else:
        print("EMPTY")