n = int(input())
a = list(map(int, input().split()))
mn = a[ 0]
idx = 0
for i in range(n):
    if a[i]< mn:
        mn = a[i]
        idx = i
print(idx)        