n = int(input())
v = [input().strip() for _ in range(n)]
print(max(v, key=v.count))