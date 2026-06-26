a, b = map(int, input().split())
amal = int(input())
if a < 0 or b < 0:
    print("Invalid")
elif (amal == 4 or amal == 5) and b == 0:
    print("Error")
else:
    if amal == 1:
        print(a + b)
    elif amal == 2:
        print(a - b)
    elif amal == 3:
        print(a * b)
    elif amal == 4:
        print(a / b)
    elif amal == 5:
        print(a % b)
    elif amal == 6:
        print(a ** b)