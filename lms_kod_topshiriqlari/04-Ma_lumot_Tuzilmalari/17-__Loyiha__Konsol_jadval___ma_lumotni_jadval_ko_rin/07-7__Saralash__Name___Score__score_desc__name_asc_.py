import sys
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    students = []
    idx = 1
    for _ in range(n):
        name = input_data[idx]
        score = int(input_data[ idx + 1])
        students.append((name, score))
        idx += 2
    students.sort(key=lambda x: (-x[1], x[0]))  
    print(f"{'Name':<10} | {'Score':>5}")
    print("-" * 10 + "+" + "-" * 5)
    for name, score in students:
        print(f"{name:<10} | {score:>5}")
if __name__ == '__main__':
    main()