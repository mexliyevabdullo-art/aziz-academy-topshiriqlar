soz = input()
unlilar_soni = 0
unli_harflar = "aeiou"
for harf in soz:
    if harf in unli_harflar:
        unlilar_soni += 1
print(unlilar_soni)        