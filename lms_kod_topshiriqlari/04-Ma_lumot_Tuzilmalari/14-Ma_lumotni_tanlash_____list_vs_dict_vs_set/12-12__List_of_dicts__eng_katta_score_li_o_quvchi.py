import sys
data = sys.stdin.read().split()
if data:
    n = int(data[0])
    students = [{'name': data[i], 'score': int(data[i+1])} for i in range(1, 2 * n, 2)]
    best = max(students, key=lambda s: (s['score'], [-ord(c) for c in s['name']]))
    print(best['name'], best['score'])