import sys
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    count = 0
    limit = min(n + 1, len(input_data))
    for i in range(1, limit):
        son = int(input_data[i])
        if son % 3 == 0:
            count += 1
    print(count)
if __name__ == '__main__':
    main()