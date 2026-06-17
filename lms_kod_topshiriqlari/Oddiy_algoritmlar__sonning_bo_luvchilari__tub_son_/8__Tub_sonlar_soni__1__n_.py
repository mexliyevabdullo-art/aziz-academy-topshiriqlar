n = int(input())
cnt = 0
for i in range(2, n + 1):
    tub = True
    for j in range(2, i):
        if i % j == 0:
            tub = False
            break
    if tub:
        cnt += 1
print(cnt)        