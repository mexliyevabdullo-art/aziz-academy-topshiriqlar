tub_sonlar_soni = 0
while True:
    son = int(input())
    if son == 0:
        break
    if son < 2:
        continue
    tub = True
    bo_luvchi = 2
    while bo_luvchi < son:
        if son % bo_luvchi == 0:
            tub = False
            break
        bo_luvchi += 1
    if tub:
        tub_sonlar_soni += 1
print(tub_sonlar_soni)        