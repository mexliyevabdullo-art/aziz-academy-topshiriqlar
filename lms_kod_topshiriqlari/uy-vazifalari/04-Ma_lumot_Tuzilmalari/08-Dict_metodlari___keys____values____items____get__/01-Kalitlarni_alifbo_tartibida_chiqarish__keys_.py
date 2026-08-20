n = int(input())
d = {}
for _ in range(n):
    name, grade = input().split()
    d[name] = grade
print(*(sorted(d.keys())))