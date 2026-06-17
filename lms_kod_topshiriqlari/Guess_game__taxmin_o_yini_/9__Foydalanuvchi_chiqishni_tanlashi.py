while True:
    n = int(input())
    if n == 0:
        print("Exit")
        break
    elif n < 3:
        print("Low")
    elif n > 3:    
        print("High")
    else:    
        print("Correct")
        break