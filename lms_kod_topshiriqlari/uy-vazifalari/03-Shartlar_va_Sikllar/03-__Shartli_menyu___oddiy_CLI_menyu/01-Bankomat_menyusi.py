amal = int(input())
balans = int(input())
summa = int(input())
if amal == 1:
    print(balans)
elif amal == 2:
    if summa <= balans:
        yangi_balans = balans - summa
        print(yangi_balans)
    else:
        print("Mablag' yetarli emas")
elif amal == 3:
    yangi_balans = balans + summa 
    print(yangi_balans)
else:
    print("Notogri amal")