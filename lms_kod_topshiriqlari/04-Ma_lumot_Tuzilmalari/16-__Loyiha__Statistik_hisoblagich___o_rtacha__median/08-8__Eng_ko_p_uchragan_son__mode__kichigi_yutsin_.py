from collections import Counter
sonlar = list(map(int, input().split()))
sanoq = Counter(sonlar)
eng_kop = max(sanoq.values())
eng_kichik = min(son for son, son_sanoq in sanoq.items() if son_sanoq == eng_kop)
print(eng_kichik)