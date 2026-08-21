# INPUT:
# n (mahsulotlar soni)
# n qator: name price qty
# Har mahsulot dict: {'name':..., 'price':..., 'qty':...}
# Vazifa: umumiy summa = Σ(price*qty)

n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})

# TODO
total = sum(item['price'] * item['qty'] for item in items)
print(total)