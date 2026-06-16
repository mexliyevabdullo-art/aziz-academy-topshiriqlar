n = int(input())
a = list(map(int, input().split()))
yigindi = 0
for x in a:
    if x > 0:
        yigindi += x
print(yigindi)        