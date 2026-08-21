a, b = set(input().split()), set(input().split())
print(*(sorted(int(x) for x in a - b)))