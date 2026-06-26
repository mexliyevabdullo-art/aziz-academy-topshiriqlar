secret = 11
tries = 0
while True:
    x = int(input())
    tries += 1
    if x == secret:
        print(tries)
        break