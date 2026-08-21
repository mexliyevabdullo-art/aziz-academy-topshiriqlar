# N ta mahsulot
# Mahsulotlarni narx bo‘yicha o‘sish tartibida chiqarish
# Har qator: name price

n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
# TODO
sorted_products = sorted(products, key=lambda p: p['price'])
for p in sorted_products:
    print(f"{p['name']} {p['price']}")