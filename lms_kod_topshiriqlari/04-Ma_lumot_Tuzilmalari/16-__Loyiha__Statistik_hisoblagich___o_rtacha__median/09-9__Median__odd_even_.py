sonlar = sorted(map(int, input().split()))
n = len(sonlar)
if n % 2 != 0:
    print(f"{sonlar[n // 2]:.2f}")
else:
    print(f"{(sonlar[n // 2 - 1] + sonlar[n // 2]) / 2:.2f}")