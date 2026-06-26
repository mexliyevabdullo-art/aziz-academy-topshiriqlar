n = int(input())
a = list(map(int, input().split()))
mx = None
for x in a:
    if x % 2 != 0:
        if mx is None or x > mx:
            mx = x
if mx is None:
    print("No")
else:
    print(mx)