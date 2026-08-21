# N ta mahsulot
# Keyin mahsulot nomi X
# Agar bor bo‘lsa YES, bo‘lmasa NO

n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
x = input().strip()
# TODO
found = any(p['name'] == x for p in products)
print("YES" if found else "NO")