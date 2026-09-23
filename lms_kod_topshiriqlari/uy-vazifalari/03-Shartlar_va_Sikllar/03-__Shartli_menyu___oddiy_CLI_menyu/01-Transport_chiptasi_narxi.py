t, k = int(input()), int(input())
if t not in [1, 2, 3]: print("Notohgri transport")
elif k not in [1, 2, 3]: print("Notogri toifa")
else:
    p = 4000 if t == 3 else 1700
    print(0 if k == 3 else p // 2 if k == 2 else p)