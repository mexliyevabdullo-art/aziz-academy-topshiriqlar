import sys
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    musbat_yigindi = 0
    for i in range(1, n + 1):
        son = int(input_data[i])
        if son > 0:
            musbat_yigindi += son
    print(musbat_yigindi)
if __name__ == '__main__':
    main()
    