n = int(input())
a = list(map(int, input().split()))
mn = None 
for x in a:
    if x % 2 == 0:
        if mn is None or x < mn:
            mn = x
if mn is None:
    print("No")
else:
    print(mn)
    