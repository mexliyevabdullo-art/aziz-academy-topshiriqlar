sonlar = list(map(int, input().split()))
print(f"{sum(sonlar) / len(sonlar):.2f}")
print(max(sonlar) - min(sonlar))