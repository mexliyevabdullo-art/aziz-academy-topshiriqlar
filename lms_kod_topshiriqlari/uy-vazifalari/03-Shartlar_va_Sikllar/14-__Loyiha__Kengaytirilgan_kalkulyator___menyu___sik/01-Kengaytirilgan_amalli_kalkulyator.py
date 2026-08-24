import sys
def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    results = []
    while idx < len(data):
        op = int(data[idx])
        if op == 0:
            break
        a = int(data[idx+1])    
        b = int(data[idx+2])
        idx += 3
        if (op == 4 or op == 6) and b == 0:
            continue
        res = None
        if op == 1:
            res = a + b 
        elif op == 2:
            res = a - b 
        elif op == 3:
            res = a * b 
        elif op == 4:
            res = a // b 
        elif op == 5:
            res = a ** b 
        elif op == 6:
            res = a % b 
        if res is not None:
            results.append(res)
    for r in results:
        print(r)
    if results:
        print(f"Eng katta natija: {max(results)}")
if __name__ == '__main__':
    solve()