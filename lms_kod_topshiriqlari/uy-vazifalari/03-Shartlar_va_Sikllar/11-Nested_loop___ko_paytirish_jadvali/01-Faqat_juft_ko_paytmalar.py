n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        product = i * j
        if product % 2 == 0:
            print(f"{i} x {j} = {product}")