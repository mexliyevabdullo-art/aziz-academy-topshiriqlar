n = int(input())
a = list(map(int, input().split()))
yigindi = 0
count = 0
for x in a:
    yigindi += x
    count += 1
print(yigindi / count)    