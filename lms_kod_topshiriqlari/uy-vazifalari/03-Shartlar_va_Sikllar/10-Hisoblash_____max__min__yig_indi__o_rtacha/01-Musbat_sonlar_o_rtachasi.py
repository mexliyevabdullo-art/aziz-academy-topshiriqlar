def main():
    n = int(input())
    positive_sum = 0
    positive_count = 0
    for _ in range(n):
        num = int(input())
        if num > 0:
            positive_sum += num
            positive_count += 1
    if positive_count > 0:
        print(positive_sum // positive_count)
    else:
        print(0)
if __name__ == '__main__':
    main()