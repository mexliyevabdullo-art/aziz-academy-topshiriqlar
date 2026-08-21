l = []
for _ in range(int(input())):
    i, m, f = input().split()
    l.append({"ism": i, "mat": int(m), "fiz": int(f)})
for x in l:
    print(x["ism"], x["mat"] + x["fiz"])