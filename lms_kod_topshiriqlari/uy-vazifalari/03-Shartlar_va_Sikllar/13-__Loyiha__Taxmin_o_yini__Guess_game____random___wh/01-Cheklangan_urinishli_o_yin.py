def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    secret = int(data[idx]); idx += 1
    n = int(data[idx]); idx += 1
    for i in range(n):
        guess = int(data[idx]); idx += 1
        if guess == secret:
            print("TOPDINGIZ")
            return
        elif guess < secret:
            print("KICHIK")
        else:
            print("KATTA")
    print("YUTQAZDINGIZ")        
main()    