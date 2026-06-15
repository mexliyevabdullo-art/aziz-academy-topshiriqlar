n = int(input())
lst = list(map(int, input().split()))
x = int(input())
for i in range(len(lst)):
    if lst[i] == x:
        print(i)
        break
else:
    print(-1)