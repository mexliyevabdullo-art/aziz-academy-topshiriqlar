x = input().split()
if len(x) == 1:
    print(x[0])
else:
    n, m = map(int, x)
    for i in range(n):
        print(*range(1, m + 1))