a = input().strip()
b = input().strip()
common_chars = set(a) & set(b)
if common_chars:
    print("".join(sorted(common_chars)))
else:
    print("BO'SH")