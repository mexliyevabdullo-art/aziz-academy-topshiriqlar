my_set = set(map(int, input().split()))
target = int(input())
if target in my_set:
    print("Bor")
else:
    print("Yo'q")