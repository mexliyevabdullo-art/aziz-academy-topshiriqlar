import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    product = []
    idx = 1
    for _ in range(n):
        name = input_data[idx]
        qty = int(input_data[idx+1])
        price = int(input_data[idx+2])
        idx += 3
        total = qty * price
        product.append((name, qty, price, total))
    print(f"{'Product':<12} | {'Qty':>3} | {'Price':>5} | {'Total':>7}")
    print("-" * 12 + "+" + "-" * 5 + "+" + "-" * 7 + "+" + "-" * 9)
    for name, qty, price, total in product:
        print(f"{name:<12} | {qty:>3} | {price:>5} | {total:>7}")
        best_product = max(product, key=lambda x: (x[3], [-ord(c) for c in x[1]]))
        best = min(product, key=lambda x: (-x[3], x[1]))
        print(f"BEST: {best[0]} {best[3]}")
    if __name__ == '__main__':
        solve()