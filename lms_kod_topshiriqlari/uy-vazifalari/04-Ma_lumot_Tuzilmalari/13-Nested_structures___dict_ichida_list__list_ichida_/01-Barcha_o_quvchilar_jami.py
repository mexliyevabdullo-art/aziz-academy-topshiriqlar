import sys
def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    n = int(input_data[0].strip())
    total_students = 0
    for i in range(1, n + 1):
        line = input_data[i].strip()
        if not line:
            continue
        parts = line.split()
        students = parts[1:]
        total_students += len(students)
    print(total_students)
if __name__ == '__main__':
    solve()