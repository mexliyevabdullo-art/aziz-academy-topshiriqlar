n = int(input())
birinchi_son = None
for _ in range(n):
    son = int(input())
    if son % 7 == 0 and birinchi_son is None:
        birinchi_son = son
if birinchi_son is not None:
    print(birinchi_son)
else:
    print("yo'q")