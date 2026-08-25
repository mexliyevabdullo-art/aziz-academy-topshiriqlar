import sys
def solve():
    words = sys.stdin.read().split()
    if not words:
        return
    print(*(words[:3]))
if __name__ == '__main__':
    solve()