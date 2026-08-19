A = set(map(int, input().split()))
B = set(map(int, input().split()))
intersection = len(A & B)
union = len(A | B)
jaccard = intersection / union
print(f"{jaccard:.3f}")