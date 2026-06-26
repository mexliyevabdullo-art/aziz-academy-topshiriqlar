while True:
    n = int(input())
    if n == 15:
        print("Correct")
        break
    elif abs(n - 15) >= 5:
        print("Far")
    else:
        print("Close")
       