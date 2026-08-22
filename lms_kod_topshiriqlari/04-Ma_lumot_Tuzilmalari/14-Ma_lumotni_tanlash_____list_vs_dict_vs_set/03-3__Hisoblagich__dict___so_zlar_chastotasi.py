words  = input().lower().split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1 
for word in sorted(counts.keys()):
    print(word, counts[word])