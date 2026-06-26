n = int(input())
arr = list(map(int, input().split()))
mn = arr[0]
for x in arr:
    if x < mn:
        mn = x
print(mn)        