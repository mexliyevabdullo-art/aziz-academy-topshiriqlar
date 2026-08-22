n = int(input())
guruhlar = {}
for _ in range(n):
    qator = input().split()
    guruh_nomi = qator[0]
    oqquvchilar = qator[1:]
    guruhlar[guruh_nomi] = oqquvchilar
for guruh, oqquvchilar in guruhlar.items():
    print(guruh, len(oqquvchilar))