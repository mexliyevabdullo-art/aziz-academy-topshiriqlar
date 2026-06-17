tries = 0
while True:
    n = int(input())
    tries += 1
    if n == 1:
        print("Correct")
        print(tries)
        break
    else:
        print("Try again")