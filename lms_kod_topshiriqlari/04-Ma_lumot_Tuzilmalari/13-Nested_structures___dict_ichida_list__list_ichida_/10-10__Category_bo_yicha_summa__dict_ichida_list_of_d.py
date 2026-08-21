# INPUT:
# n
# n qator: category name price qty
# Vazifa: har category bo‘yicha total sum = Σ(price*qty)
# Output: categorylar alifbo bo‘yicha sort bo‘lsin
# Har qator: category total

n = int(input().strip())
items = []
for _ in range(n):
    cat, name, price, qty = input().split()
    items.append({'cat': cat, 'name': name, 'price': int(price), 'qty': int(qty)})

# TODO
categories = {}
for item in items:
    cat = item['cat']
    total = item['price'] * item['qty']
    categories[cat] = categories.get(cat, 0) + total
for cat in sorted(categories):
    print(cat, categories[cat])