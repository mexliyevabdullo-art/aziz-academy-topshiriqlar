n, m = map(int, input().split())
for x in range(n, m + 1):
    print(x, end=" " if x < m else "")