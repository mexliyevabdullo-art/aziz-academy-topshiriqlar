import sys
data = sys.stdin.read().split()
yashirin = int(data[0])
taxminlar = list(map(int, data[1:]))
urinishlar = 0
for t in taxminlar:
    urinishlar += 1
    if t == yashirin:
        print("TOPDINGIZ")
        break
    elif t > yashirin:
        print("KATTA")
    else:
        print("KICHIK")
print(f"Urinishlar: {urinishlar}")        