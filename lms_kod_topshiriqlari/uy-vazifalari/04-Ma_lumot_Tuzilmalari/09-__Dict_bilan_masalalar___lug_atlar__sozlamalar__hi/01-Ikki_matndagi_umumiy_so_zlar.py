import sys
def solve():
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2:
        return
    set1 = set(lines[0].split())
    set2 = set(lines[1].split())
    umumiy = set1.intersection(set2)
    for soz in sorted(umumiy):
        print(soz)
if __name__ == '__main__':
    solve()