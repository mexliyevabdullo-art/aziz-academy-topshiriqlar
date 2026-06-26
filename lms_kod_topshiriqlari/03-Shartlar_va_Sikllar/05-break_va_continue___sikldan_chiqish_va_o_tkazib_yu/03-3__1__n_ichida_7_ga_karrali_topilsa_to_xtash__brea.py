n = int(input())
i = 1
while i <= n:
    if i % 7 == 0:
        print(i)
        break
    i += 1 
if i > n:
    print("No")