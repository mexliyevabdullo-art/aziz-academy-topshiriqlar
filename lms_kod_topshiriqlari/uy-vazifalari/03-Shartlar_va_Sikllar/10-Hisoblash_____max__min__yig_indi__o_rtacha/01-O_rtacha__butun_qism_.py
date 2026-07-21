def main():
    n = int(input())
    total = 0
    for _ in range(n):
        total += int(input())
    print(total // n)
if __name__ == '__main__':
    main()