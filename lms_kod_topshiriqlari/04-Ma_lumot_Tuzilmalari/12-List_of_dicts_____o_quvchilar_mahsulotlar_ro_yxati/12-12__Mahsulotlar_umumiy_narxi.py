# N ta mahsulot
# Umumiy narxni chiqaring

n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
# TODO
total_price = sum(p['price'] for p in products)
print(total_price)