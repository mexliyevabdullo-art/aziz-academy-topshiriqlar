import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    sonlar = [int(x) for x in input_data]
    sanoq = {}
    for son in sonlar:
        sanoq[son] = sanoq.get(son, 0) + 1
    eng_takror = max(sanoq.values())
    eng_koplar = [son for son, count in sanoq.items() if count == eng_takror]
    print(min(eng_koplar))
if __name__ == '__main__':
    solve()
