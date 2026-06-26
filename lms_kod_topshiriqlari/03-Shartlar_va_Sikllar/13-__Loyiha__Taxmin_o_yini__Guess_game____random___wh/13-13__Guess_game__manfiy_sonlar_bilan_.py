while True:
    n = int(input())
    if n < -4:
        print("Low")
    elif n > -4:
        print("High")
    else:
        print("Correct")
        break