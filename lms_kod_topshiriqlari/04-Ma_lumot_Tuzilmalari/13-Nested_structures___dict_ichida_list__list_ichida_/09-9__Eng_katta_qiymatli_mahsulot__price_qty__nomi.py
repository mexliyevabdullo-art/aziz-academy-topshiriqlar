# INPUT:
# n
# n qator: name price qty
# Har mahsulot qiymati = price*qty
# Vazifa: eng katta qiymatli mahsulot nomini chiqaring.
# Agar teng bo‘lsa: birinchi uchragani.

n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})

# TODO
best_item = max(items, key=lambda x: x['price'] * x['qty'])
print(best_item['name'])