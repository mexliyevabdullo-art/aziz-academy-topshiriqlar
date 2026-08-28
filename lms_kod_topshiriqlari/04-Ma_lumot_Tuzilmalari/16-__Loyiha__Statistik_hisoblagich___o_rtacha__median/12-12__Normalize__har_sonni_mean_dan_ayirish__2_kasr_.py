sonlar = list(map(int, input().split()))
mean = sum(sonlar) / len(sonlar)
print(*(f"{x - mean:.2f}" for x in sonlar))