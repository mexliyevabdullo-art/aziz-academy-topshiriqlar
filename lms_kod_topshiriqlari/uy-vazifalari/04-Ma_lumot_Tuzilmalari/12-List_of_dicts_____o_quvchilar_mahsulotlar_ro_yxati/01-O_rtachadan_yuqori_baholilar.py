n = int(input())
d = []
for _ in range(n):
    ism, baho = input().split()
    d.append({"ism": ism, "baho": int(baho)})
orta = sum(x["baho"] for x in d) / n 
for x in d:
    if x["baho"] > orta:
        print(x["ism"])