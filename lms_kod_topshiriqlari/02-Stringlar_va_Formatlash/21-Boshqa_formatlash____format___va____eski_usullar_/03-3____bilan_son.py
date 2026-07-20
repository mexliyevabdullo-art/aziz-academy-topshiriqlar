import sys
def main():
    input_data = sys.stdin.read().split()
    if input_data:
        yosh = int(input_data[0])
        print("Yosh: %d" % yosh)
if __name__ == '__main__':
    main()