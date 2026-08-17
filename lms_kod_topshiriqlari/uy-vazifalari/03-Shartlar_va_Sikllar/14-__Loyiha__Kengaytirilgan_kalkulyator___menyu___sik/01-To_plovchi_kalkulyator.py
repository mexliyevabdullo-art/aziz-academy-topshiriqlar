import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        print(0)
        return
    result = 0
    i = 0
    while i < len(input_data):
        op = input_data[i]
        if op == '=':
            break
        if i + 1 < len(input_data):
            num = int(input_data[i + 1])
            if op == '+':
                result += num
            elif op == '-':
                result -= num
            elif op == '*':
                result *= num
            elif op == '/':
                if num != 0:
                    result //= num
            i += 2
        else:
            break
    print(result)
if __name__ == '__main__':
    solve()