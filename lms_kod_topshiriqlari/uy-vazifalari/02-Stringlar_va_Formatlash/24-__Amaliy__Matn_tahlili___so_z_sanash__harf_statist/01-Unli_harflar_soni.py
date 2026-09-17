matn = input().lower()
unilar = 'aeiou'
natija = sum(matn.count(harf) for harf in unilar)
print(natija)