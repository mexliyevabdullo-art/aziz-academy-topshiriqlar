secret = 20
tries = 0
while True:
    x = int(input())
    tries += 1
    if x < 1 or x > 20:
        print("Invalid")
    elif x < secret:    
        print("Low")
    elif x > secret:
        print("High")
    else:
        print("Correct")
        print(tries)
        break