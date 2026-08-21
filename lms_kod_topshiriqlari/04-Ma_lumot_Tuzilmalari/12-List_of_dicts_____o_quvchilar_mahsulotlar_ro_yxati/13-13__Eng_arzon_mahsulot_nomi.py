# N ta mahsulot
# Eng arzon mahsulot nomini chiqaring

n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
# TODO
cheapst = min(products, key=lambda p: p['price'])
print(cheapst['name'])