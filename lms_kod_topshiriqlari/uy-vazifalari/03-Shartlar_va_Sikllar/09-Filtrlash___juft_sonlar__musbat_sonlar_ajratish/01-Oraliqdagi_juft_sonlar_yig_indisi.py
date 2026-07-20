import sys
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a = int(input_data[0])
    b = int(input_data[1])
    yigindi = 0
    for son in range(a, b + 1):
        if son % 2 == 0:
            yigindi += son
    print(yigindi)
if __name__  == '__main__':
    main()