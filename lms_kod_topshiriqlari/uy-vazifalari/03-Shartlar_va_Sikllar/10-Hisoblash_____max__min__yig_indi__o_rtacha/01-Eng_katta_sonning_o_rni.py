def main():
    n = int(input())
    max_val = int(input())
    max_pos = 1
    for pos in range(2, n + 1):
        num = int(input())
        if num > max_val:
            max_val = num
            max_pos = pos
            
    print(max_pos)
if __name__ == '__main__':
    main()