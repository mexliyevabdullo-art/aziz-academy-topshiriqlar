# INPUT:
# n
# n qator: name price qty
# Vazifa: eng katta price ga ega mahsulot nomini chiqaring.
# Agar teng bo‘lsa: birinchi uchraganini chiqaring.

n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})

# TODO
best_item = max(items, key=lambda x: x['price'])
print(best_item['name'])