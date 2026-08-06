n = int(input())
k = int(input())
for _ in range(k):
    guess = int(input())
    if guess == n:
        print("TOPDINGIZ")
    elif guess > n:
        print("KATTA")
    else:
        print("KICHIK")