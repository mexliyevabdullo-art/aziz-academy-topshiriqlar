import sys
def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    n = int(input_data[0].strip())

    for i in range(1, n + 1):
        parts = input_data[i].split()
        name = parts[0]
        score = parts[1]
        print(f"{i}|{name}|{score}")
if __name__ == '__main__':
    solve()