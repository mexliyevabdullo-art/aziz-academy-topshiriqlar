seen = set()
for x in input().split():
    if x in seen:
        print(x)
        break
    seen.add(x)
else:
    print("Yo'q")