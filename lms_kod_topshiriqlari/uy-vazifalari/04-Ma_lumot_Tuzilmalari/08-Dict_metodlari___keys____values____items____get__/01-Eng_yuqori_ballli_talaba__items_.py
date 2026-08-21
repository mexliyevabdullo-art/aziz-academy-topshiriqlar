n = int(input())
d = {}
for _ in range(n):
    name, score = input().split()
    d[name] = int(score)
best_name, best_score = sorted(d.items(), key=lambda x: (-x[1], x[0]))[0]
print(best_name, best_score)