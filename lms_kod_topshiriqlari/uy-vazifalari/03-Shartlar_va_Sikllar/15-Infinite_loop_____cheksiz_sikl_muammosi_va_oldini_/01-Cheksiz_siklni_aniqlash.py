start = int(input())
step = int(input())
if step <= 0:
    print("CHEKSIZ")
else:
    steps_count = 0
    current = start
    while current < 100:
        current += step 
        steps_count += 1
    print(steps_count)    