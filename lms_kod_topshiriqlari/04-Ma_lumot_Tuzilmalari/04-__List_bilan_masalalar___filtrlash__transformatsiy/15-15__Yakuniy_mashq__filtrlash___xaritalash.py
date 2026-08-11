n = int(input())
print([x * 2 for x in map(int, input().split()) if x > 0])