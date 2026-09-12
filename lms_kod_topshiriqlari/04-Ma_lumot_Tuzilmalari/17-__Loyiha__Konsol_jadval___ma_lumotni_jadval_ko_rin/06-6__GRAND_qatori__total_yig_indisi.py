import sys
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    items = []
    index = 1
    for _ in range(n):
        product = input_data[index]
        qty = int(input_data[index + 1])
        price = int(input_data[index + 2])
        index += 3
        items.append((product, qty, price))
    print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}") 
    print("-" * 12 + "+" + "-" * 5 + "+" + "-" * 7 + "+" + "-" * 9)
    grand_total = 0
    for product, qty, price in items:
        total = qty * price
        grand_total += total
        print(f"{product:<12} | {qty:>5} | {price:>7} | {total:>9}")
    print(f"GRAND: {grand_total}") 
if __name__ == '__main__':
    main()