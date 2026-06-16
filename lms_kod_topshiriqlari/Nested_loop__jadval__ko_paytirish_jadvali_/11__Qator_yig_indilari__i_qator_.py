n, m = map(int, input().split())
for i in range(1, n + 1):
    row_sum = 0
    for j in range(1, m + 1):
        row_sum += i * j
    print(row_sum)    