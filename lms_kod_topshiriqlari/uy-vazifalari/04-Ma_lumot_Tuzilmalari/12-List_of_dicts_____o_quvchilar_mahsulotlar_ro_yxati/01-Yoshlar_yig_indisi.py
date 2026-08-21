n = int(input())
oqquvchilar = []
for _ in range(n):
    qator = input().split()
    ism = qator[0]
    yosh = int(qator[1])
    oqquvchilar.append({"ism": ism, "yosh": yosh})
yigindi = sum(oquvchi["yosh"] for oquvchi in oqquvchilar)
print(yigindi)