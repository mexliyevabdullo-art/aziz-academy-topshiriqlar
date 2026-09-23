a, b, c = int(input()), int(input()), int(input())
print(b if a==1 else (b-c if b>=c else "Mablag' yetarli emas") if a==2 else b+c if a==3 else "Notogri amal")