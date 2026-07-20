import sys
def main():
    data = sys.stdin.read().split()
    if len(data) >= 2:
        ism = data[0]
        yosh = data[1]
        print("{} {} yosh".format(ism, yosh))
if __name__ == '__main__':
    main()