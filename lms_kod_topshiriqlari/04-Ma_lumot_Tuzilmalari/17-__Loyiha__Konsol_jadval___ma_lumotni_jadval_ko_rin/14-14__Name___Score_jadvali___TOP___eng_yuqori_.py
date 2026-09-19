import sys
def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    n = int(input_data[0].strip())
    data = []
    for i in range(1, n + 1):
        line = input_data[i].strip()
        if not line:
            continue
        parts = line.split()
        name = parts[0]
        score = int(parts[1])
        data.append((name, score))
    print("Name       | Score") 
    print("----------+-----")
    max_score = -1
    top_name = ""
    for name, score in data:
        print(f"{name:<10} | {score:>5}")
        if score > max_score or (score == max_score and name < top_name):
            max_score = score
            top_name = name
    print(f"TOP: {top_name} {max_score}") 
if __name__ == '__main__':
    solve()