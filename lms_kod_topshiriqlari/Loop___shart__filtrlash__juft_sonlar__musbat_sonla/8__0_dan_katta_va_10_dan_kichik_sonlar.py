n = int(input())
a = list(map(int, input().split()))
for x in a:
    if 0 < x < 10:
        print(x)