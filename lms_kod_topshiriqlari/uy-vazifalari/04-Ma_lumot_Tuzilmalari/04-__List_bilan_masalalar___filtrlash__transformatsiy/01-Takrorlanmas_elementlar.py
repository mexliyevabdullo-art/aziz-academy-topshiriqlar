element = input().split()
result = []
for x in element:
    if x not in result:
        result.append(x)
print(*result)        