n = int(input())
m = []
for _ in range(n):
    nom, narx = input().split()
    m.append({"nom": nom, "narx": int(narx)})
l = int(input())
for x in m:
    if x["narx"] < l:
        print(x["nom"])