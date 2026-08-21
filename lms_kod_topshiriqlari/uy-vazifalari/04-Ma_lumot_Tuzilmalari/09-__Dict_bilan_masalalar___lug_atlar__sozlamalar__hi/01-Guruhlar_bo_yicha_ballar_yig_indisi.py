import sys 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    guruhlar = {}
    idx = 1
    for _ in range(n):
        guruh = input_data[idx]
        ball = int(input_data[idx+1])
        idx += 2 
        guruhlar[guruh] = guruhlar.get(guruh, 0) + ball 
    for guruh in sorted(guruhlar.keys()) :
        print(f"{guruh} {guruhlar[guruh]}")
if __name__ == '__main__':
    solve()