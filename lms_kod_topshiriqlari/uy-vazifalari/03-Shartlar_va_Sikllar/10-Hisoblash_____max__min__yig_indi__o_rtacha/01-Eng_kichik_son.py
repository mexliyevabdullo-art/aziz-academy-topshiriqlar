import sys
def main():
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        print(min(map(int, data[1 : n + 1])))
if __name__ == '__main__':
    main()