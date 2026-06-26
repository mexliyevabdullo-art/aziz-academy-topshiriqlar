for _ in range(2):
    a, b = map(int, input().split())
    amal = int(input())
    if amal == 1:
        print(a + b)
    elif amal == 2:
        print(a - b)
    elif amal == 3:
        print(a * b)
    elif amal == 4:
        print(a / b)
input()
print("Exit")