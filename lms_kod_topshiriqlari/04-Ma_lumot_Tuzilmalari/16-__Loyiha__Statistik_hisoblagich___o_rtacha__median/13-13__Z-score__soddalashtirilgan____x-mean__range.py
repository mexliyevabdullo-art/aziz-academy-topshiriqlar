sonlar = list(map(int, input().split()))
mean = sum(sonlar) / len(sonlar)
rng = max(sonlar) - min(sonlar)
if rng == 0:
    print(*(f"{0.00:.2f}" for _ in sonlar))
else:
    print(*(f"{(x - mean) / rng:.2f}" for x in sonlar))