n = int(input())
topildi = False
for _ in range(n):
    son = int(input())
    if not topildi and son % 7 == 0:
        print(son)
        topildi = True
        break
if not topildi:
    print("yo'q")