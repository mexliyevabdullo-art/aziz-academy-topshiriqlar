n = int(input())
items = []
for _ in range(n):
    line = input().split()
    product = line[0]
    qty = int(line[1])
    price = int(float(line[2]))
    total = qty * price
    items.append((product, qty, price, total))
print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}")
print("-" * 12 + "+-" + "-"* 5 + "+-" + "-" * 7 + "+-" + "-" * 9)
for product, qty, price, total in items:
    print(f"{product:<12} | {qty:>5} | {price:>7} | {total:>9}")