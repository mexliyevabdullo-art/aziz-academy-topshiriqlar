n = int(input())
a = list(map(int, input().split()))
k = int(input())
yaqin = a[0]
for x in a:
    if abs(x - k) < abs(yaqin - k):
        yaqin = x
    elif abs(x - k) == abs(yaqin - k) and x < yaqin:
        yaqin = x
print(yaqin)        