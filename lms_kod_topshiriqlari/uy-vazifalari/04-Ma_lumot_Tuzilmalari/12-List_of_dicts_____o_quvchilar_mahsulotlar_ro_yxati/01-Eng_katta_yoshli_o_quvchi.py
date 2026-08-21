o = []
for _ in range(int(input())):
    i, y = input().split()
    o.append({"ism": i, "yosh": int(y)})
print(max(o, key=lambda x: x["yosh"])["ism"])    