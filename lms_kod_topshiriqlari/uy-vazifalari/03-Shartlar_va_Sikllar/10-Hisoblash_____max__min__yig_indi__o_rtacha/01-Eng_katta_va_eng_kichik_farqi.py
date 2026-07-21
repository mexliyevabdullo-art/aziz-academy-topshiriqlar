def main():
    n = int(input())
    first_num = int(input())
    max_val = first_num
    min_val = first_num
    for _ in range(n - 1):
        num = int(input())
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    print(max_val - min_val)
if __name__ == '__main__':
    main()