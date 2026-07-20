import sys
def main():
    input_data = sys.stdin.read().split()
    if input_data:
        ism = input_data[0]
        print("Ism: %s" % ism)
if __name__ == '__main__':
    main()