import sys
def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    scores = {}
    idx = 1
    for _ in range(n):
        name = data[idx]
        score = data[idx+1]
        scores[name] = score 
        idx += 2
    m = int(data[idx])
    idx += 1
    for _ in range(m):
        query_name = data[idx]
        idx += 1
        if query_name in scores:
            print(scores[query_name])
        else:
            print("NOT_FOUND")
if __name__ == '__main__':
    solve()