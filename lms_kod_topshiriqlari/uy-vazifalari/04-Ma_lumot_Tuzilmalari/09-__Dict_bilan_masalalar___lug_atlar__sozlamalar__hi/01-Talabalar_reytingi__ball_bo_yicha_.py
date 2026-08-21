import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    students = []
    idx = 1
    for _ in range(n):
        name = input_data[idx]
        score = int(input_data[idx+1])
        idx += 2
        students.append({'name': name, 'score': score})
    sorted_students = sorted(students, key=lambda x: (-x['score'], x['name']))
    for s in sorted_students:
        print(f"{s['name']} {s['score']}")
if __name__ == '__main__':
    solve()