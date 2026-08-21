# N ta mahsulot: name price
# Mahsulotlar sonini chiqaring

n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
# TODO
print(len(products))