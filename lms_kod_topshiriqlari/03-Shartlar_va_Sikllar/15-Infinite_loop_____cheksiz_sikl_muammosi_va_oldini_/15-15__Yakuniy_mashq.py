x = input()
if x == "hello":
    y = input()
    if y == "stop":
        print("Working")
else:
    n = int(x)
    a = list(map(int, input().split()))
    print(a[0])
    print(a[1:-1])
    print(a[-1])