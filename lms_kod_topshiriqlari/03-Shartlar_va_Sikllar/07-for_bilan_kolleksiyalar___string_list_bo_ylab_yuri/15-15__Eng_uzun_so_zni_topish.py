words = input().split()
max_word = words[0]
for w in words:
    if len(w) > len(max_word):
        max_word = w
print(max_word)        