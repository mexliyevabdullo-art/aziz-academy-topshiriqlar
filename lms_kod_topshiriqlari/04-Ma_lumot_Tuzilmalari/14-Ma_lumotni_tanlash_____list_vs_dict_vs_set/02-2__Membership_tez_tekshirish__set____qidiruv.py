n = int(input())
numbers = set(map(int, input().split()))
q = int(input())
for _ in range(q):
    query = int(input())
    if query in numbers:
        print("YES")
    else:
        print("NO")