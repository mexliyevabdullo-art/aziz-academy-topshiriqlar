n = int(input())
sonlar = []

for _ in range (n):
    son = int(input())
    sonlar.append(son)
    
sonlar.sort()

print(*(sonlar))