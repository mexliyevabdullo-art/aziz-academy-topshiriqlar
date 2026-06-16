n = int(input())
a = list(map(int, input().split()))
mx = 0
ans = a[0]
for x in a:
    c = a.count(x)
    if c > mx or (c == mx and x < ans):
        mx = c
        ans = x
print(ans)        