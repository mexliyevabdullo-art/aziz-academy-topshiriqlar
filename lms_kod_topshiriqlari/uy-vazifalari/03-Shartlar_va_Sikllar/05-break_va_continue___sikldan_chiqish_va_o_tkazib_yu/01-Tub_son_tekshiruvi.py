n = int(input())
if n <= 1:
    print("yo'q")
else:
    tub = True
    for i in range(2, n):
        if n % i == 0:
            tub = False
            break
    if tub:
        print("ha")
    else:
        print("yo'q")